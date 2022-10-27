# ===============================================
# ===============================================
# *\CMakeLists.txt
# ===============================================
# ===============================================

cmake_minimum_required(VERSION 3.10)

project(Win_shell_tool_lib)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_subdirectory(src)

set(SRC_MAIN main.cpp)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

add_executable(tl ${CPP_SRC_LIST} ${SRC_MAIN})
add_executable(tlnew src/tlnew.c)

#file(COPY ${PROJECT_SOURCE_DIR}/src/py_lib/dist/tltime.exe DESTINATION ${PROJECT_SOURCE_DIR}/bin)

#file(COPY ${PROJECT_SOURCE_DIR}/src/py_lib/dist/tlnew.exe DESTINATION ${PROJECT_SOURCE_DIR}/bin)
