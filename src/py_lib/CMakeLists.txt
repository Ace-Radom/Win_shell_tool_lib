# ===============================================
# ===============================================
# *\src\py_lib\CMakeLists.txt
# ===============================================
# ===============================================

set(PY_LIB ${PROJECT_SOURCE_DIR}/src/py_lib/tltime.py ${PROJECT_SOURCE_DIR}/src/py_lib/tlnew.py PARENT_SCOPE)

execute_process(COMMAND pyinstaller -F tltime.py --distpath ${PROJECT_SOURCE_DIR}/bin
                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)

#execute_process(COMMAND pyinstaller -F tlnew.py --distpath ${PROJECT_SOURCE_DIR}/bin
#                WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/src/py_lib)
