# ===============================================
# ===============================================
# *\src\py_lib\CMakeLists.txt
# ===============================================
# ===============================================

set(PY_LIB ${PROJECT_SOURCE_DIR}/src/py_lib/tltime.py PARENT_SCOPE)

execute_process(COMMAND pyinstaller -F tltime.py
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)