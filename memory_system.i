%module memory_system
%include <std_string.i>
%include <typemaps.i>

%typemap(in) uint64_t {
    $1 = (uint64_t) PyInt_AsLong($input);
}
%{
    #define SWIG_FILE_WITH_INIT
    #include "../DRAMsim3/src/configuration.h"
    #include "../DRAMsim3/src/memory_system.h"

    

%}

%include "../DRAMsim3/src/memory_system.h"
