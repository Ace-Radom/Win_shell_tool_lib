# ===============================================
# ===============================================
# *\src\CMakeLists.txt
# ===============================================
# ===============================================

add_subdirectory(py_lib)

set(src ${PROJECT_SOURCE_DIR}/src/flags.cpp)

message(STATUS "src list: " ${src})

message(STATUS "py_lib list: " ${PY_LIB})

set(CPP_SRC_LIST ${src} PARENT_SCOPE)