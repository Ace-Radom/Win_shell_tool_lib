#include<flags.h>

Commandline_Flags f;

int main( int argc , char** argv ){
    f.readin_flags( argc , argv );
    return 0;
}