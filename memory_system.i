%module memory_system
%include <std_string.i>
%include <typemaps.i>

%{
    #define SWIG_FILE_WITH_INIT
    #include "../DRAMsim3/src/configuration.h"
    #include "../DRAMsim3/src/memory_system.h"

%}

%include "../DRAMsim3/src/memory_system.h"
