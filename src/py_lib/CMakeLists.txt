# ===============================================
# ===============================================
# *\src\py_lib\CMakeLists.txt
# ===============================================
# ===============================================

set(PY_LIB ${PROJECT_SOURCE_DIR}/src/py_lib/tltime.py \n
           ${PROJECT_SOURCE_DIR}/src/py_lib/tlnew.py \n
           ${PROJECT_SOURCE_DIR}/src/py_lib/tldel.py \n
           ${PROJECT_SOURCE_DIR}/src/py_lib/tlos.py PARENT_SCOPE)

execute_process(COMMAND pyinstaller -F tltime.py
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)

execute_process(COMMAND pyinstaller -F tlnew.py
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)

execute_process(COMMAND pyinstaller -F tldel.py
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)

execute_process(COMMAND pyinstaller -F tlos.py
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)
