/**
 * ===============================================
 * ===============================================
 * *\include\flags.h
 * ===============================================
 * ===============================================
 */

#ifndef _FLAGS_H_
#define _FLAGS_H_
#pragma once

#include<string>
#include<string.h>
#include<stdint.h>
#include<iostream>

#define ROOT 0
#define CHILD 1

typedef bool STATUS_t;

struct Flags{
    std::string flag;
    std::string type;
    STATUS_t mode;
    std::string parent_flag_if_necessary;
    std::string command;
};

#define flags_num 15

class Commandline_Flags{
    public:
        void readin_flags( const int , char** );

    private:

};



#endif