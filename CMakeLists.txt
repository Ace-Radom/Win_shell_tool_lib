# ===============================================
# ===============================================
# *\CMakeLists.txt
# ===============================================
# ===============================================

cmake_minimum_required(VERSION 3.10)

project(Win_shell_tool_lib)

add_subdirectory(src)

set(SRC_MAIN main.cpp)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

add_executable(tl ${SRC_MAIN})