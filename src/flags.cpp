/**
 * ===============================================
 * ===============================================
 * *\src\flags.cpp
 * ===============================================
 * ===============================================
 */

#include<flags.h>

Flags flag_lib[] = {
    {},
    { "time" , "bool" , ROOT , "" , "tltime" },
        { "cc" , "bool" , CHILD , "time" , "--chinese_calendar=true" },
        { "ts" , "bool" , CHILD , "time" , "--timestamp=true" },
    { "new" , "bool" , ROOT , "" , "tlnew" },
        { "path" , "string" , CHILD , "new" , "--path" }, // need to add path in func readin_flags
        { "folder" , "bool" , CHILD , "new" , "--folder=true" },
        { "file" , "bool" , CHILD , "new" , "--file=true" }
};

void Commandline_Flags::readin_flags( const int _argc , char** _argv ){
    for ( int i = 0 ; i < _argc ; i++ )
    {
        for ( int sf = 1 ; sf <= flags_num ; sf++ ) // search flags
        {
            if ( ( flag_lib[sf].mode == ROOT ) && ( flag_lib[sf].flag == _argv[i] ) )
            {
                std::string command( flag_lib[sf].command );
                for ( int scf = sf ; scf <= flags_num ; scf++ ) // search child flags
                {
                    if ( flag_lib[scf].parent_flag_if_necessary == flag_lib[sf].flag )
                    {
                        for ( int spf = i ; spf < _argc ; spf++ ) // search child flags in argv
                        {
                            if ( flag_lib[scf].flag == _argv[spf] )
                            {
                                if ( flag_lib[scf].type == "bool" )
                                {
                                    command.append( " " ).append( flag_lib[scf].command );
                                }
                                if ( flag_lib[scf].type == "string" )
                                {
                                    command.append( " " ).append( flag_lib[scf].command ).append( " " ).append( _argv[spf+1] );
                                    // append the next arg after string-type flags
                                }
                            }
                        }
                    }
                }
//              std::cout << command << std::endl;
                // debug line
                system( command.c_str() );
                break;
            }
        }
    }
    return;
}