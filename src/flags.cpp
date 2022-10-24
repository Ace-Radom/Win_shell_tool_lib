#include<flags.h>

Flags flag_lib[] = {
    {},
    { "time" , ROOT , "" , ".\\tltime" },
        { "cc" , CHILD , "time" , "--chinese_calendar=true" },
        { "ts" , CHILD , "time" , "--timestamp=true" }
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
                        for ( int spf = i ; spf < _argc ; spf++ ) // search parent flags
                        {
                            if ( flag_lib[scf].flag == _argv[spf] )
                            {
                                command.append( " " ).append( flag_lib[scf].command );
                            }
                        }
                    }
                }
                std::cout << command << std::endl;
                //system( command.c_str() );
                break;
            }
        }
    }
}