%module dram_system

%{
    #define SWIG_FILE_WITH_INIT
    #include "../DRAMsim3/src/configuration.h"
    #include "../DRAMsim3/src/dram_system.h"

%}

%include "../DRAMsim3/src/dram_system.h"
