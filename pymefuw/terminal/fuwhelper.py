from enum import StrEnum

from pymeu import comms
from pymeu import types
from pymeu.terminal import helper

# Known static value for successful creation of a folder.
# Further investigation needed.
CREATE_DIR_SUCCESS = 0

# Known functions available from FuwHelper.
class FuwHelperFunctions(StrEnum):
    CREATE_FOLDER = 'CreateRemDirectory' # Args: {Folder Path}, Returns: Static value if successful [Further investigation needed]
    DELETE_FILE = 'DeleteRemFile' # Args: {File Path}, Returns: ???
    GET_EXE_RUNNING = 'IsExeRunning' # Atgs: {Process Name}, Returns: 1 if process is running, 0 otherwise
    GET_FILE_EXISTS = 'FileExists' # Args: {File Path}, Returns: {File Size} if {File Path} exists, 0 otherwise
    GET_FOLDER_EXISTS = 'StorageExists' # Args: {Folder Path}, Returns: 1 if {Folder Path} exists
    STOP_PROCESS_ME = 'SafeTerminateME' # Args: Null

def create_folder(cip: comms.Driver, paths: types.MEDevicePaths, dir: str) -> bool:
    req_args = [paths.fuw_helper_file, FuwHelperFunctions.CREATE_FOLDER, dir]
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != CREATE_DIR_SUCCESS): raise Exception(f'Failed to execute function: {req_args}, response code: {resp_code}, response data: {resp_data}.')
    return True

def delete_file(cip: comms.Driver, paths: types.MEDevicePaths, file_path: str) -> bool:
    req_args = [paths.helper_file, FuwHelperFunctions.DELETE_FILE, file_path]
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != 0): raise Exception(f'Failed to delete file on terminal: {file_path}, response code: {resp_code}, response data: {resp_data}.')
    return True

def get_exe_running(cip: comms.Driver, paths: types.MEDevicePaths, process_name: str) -> bool:
    req_args = [paths.fuw_helper_file, FuwHelperFunctions.GET_EXE_RUNNING, process_name]
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != 0): return False    
    return bool(int(resp_data))

def get_file_exists(cip: comms.Driver, paths: types.MEDevicePaths, file_path: str) -> bool:
    req_args = [paths.fuw_helper_file, FuwHelperFunctions.GET_FILE_EXISTS, file_path]
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != 0): return False    
    return bool(int(resp_data))

def get_folder_exists(cip: comms.Driver, paths: types.MEDevicePaths, folder_path: str) -> bool:
    req_args = [paths.fuw_helper_file, FuwHelperFunctions.GET_FOLDER_EXISTS, folder_path]
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != 0): return False    
    return bool(int(resp_data))

def stop_process_me(cip: comms.Driver, paths: types.MEDevicePaths) -> bool:
    req_args = [paths.fuw_helper_file, FuwHelperFunctions.STOP_PROCESS_ME, '']
    resp_code, resp_data = helper.run_function(cip, req_args)
    if (resp_code != 0): return False    
    return bool(int(resp_data))