@echo off
setlocal enabledelayedexpansion

set "source_folder="
set /p "source_folder=Enter the source folder path: "

set "output_directory=%USERPROFILE%\Downloads\Output"

if not exist "%source_folder%" (
    echo Source folder does not exist.
    pause
) else (
    call :list_files_and_folders "%source_folder%" "%output_directory%"
    echo Output saved to %output_directory%
    pause
)

exit /b

:list_files_and_folders
set "root_path=%~1"
set "output_directory=%~2"
set "output_file="

call :get_available_filename "output"

echo Root: %root_path% > "%output_file%"

call :process_folder "%root_path%" 0
exit /b

:get_available_filename
set "base_filename=output"
set "count=1"

:check_filename
set "filename=%base_filename%_%count%.txt"
set "filepath=%output_directory%\%filename%"

if exist "%filepath%" (
    set /a "count+=1"
    goto :check_filename
)

set "output_file=%filepath%"
exit /b

:process_folder
set "folder_path=%~1"
set "depth=%~2"
set "indent="

for /l %%i in (1,1,%depth%) do (
    set "indent=!indent!-"
)

for %%a in ("%folder_path%\*") do (
    if exist "%%a\" (
        echo !indent! FOLDER: %%~nxa
        call :process_folder "%%a" %depth%+1
    ) else (
        echo !indent! FILE: %%~nxa
    )
)

exit /b
