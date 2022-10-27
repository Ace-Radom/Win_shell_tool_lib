#include <errno.h>
#include <fcntl.h>
#include <libgen.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

/* define our own warning meachanisms here because err.h does not seem portable */
#define warnx(fmt, ...) (fprintf(stderr, fmt "\n", __VA_ARGS__))
#define warn(fmt, ...) (warnx(fmt ": %s", __VA_ARGS__, strerror(errno)))

/* masks for the permission of new files */
#define DPERMMASK 0755
#define FPERMMASK 0644

/* the mkdir() function on Windows differs from the POSIX mkdir() */
#ifdef _WIN32
#define mkdir(fn, mode) mkdir(fn)
#endif

static int isdir = 0;

static int create_parent(char *fn) {
	struct stat st;
	char *cfn = strdup(fn);
	if (!cfn)
		return warn("Memory allocation error while trying to create %s", fn),-1;
	char *dn = dirname(cfn);
	if (stat(dn, &st)) {
		int perm = create_parent(dn);
		if (perm < 0) {
			free(cfn);
			return perm;
		} else {
			if (mkdir(dn, perm&DPERMMASK)) {
				warn("Failed to create %s", dn);
				free(cfn);
				return -1;
			} else {
				free(cfn);
				return perm;
			}
		}
	} else {
		if (st.st_mode & S_IFDIR) {
			free(cfn);
			return st.st_mode;
		} else {
			errno = ENOTDIR;
			warn("%s", dn);
			free(cfn);
			return -1;
		}
	}
}

static void tlnew(char *fn) {
	int perm = create_parent(fn);
	if (perm < 0)
		return (void) warnx("Failed to create parent directory for %s", fn);
	if (isdir) {
		if (mkdir(fn, perm & DPERMMASK))
			warn("Failed to create directory %s", fn);
	} else {
		int fd = creat(fn, perm & FPERMMASK);
		if (!fd)
			warn("Failed to create regular file %s", fn);
		close(fd);
	}
}

int main(int argc, char **argv) {
	int opt;
	while ((opt = getopt(argc, argv, "-df")) != -1) {
		switch (opt) {
			case 'd':
				isdir = 1;
				break;
			case 'f':
				isdir = 0;
				break;
			case 1:
				tlnew(optarg);
				break;
		}
	}
	return 0;
}
