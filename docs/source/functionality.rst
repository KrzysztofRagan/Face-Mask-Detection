functionality module
====================
Functionality contains:

- choosing folder - in which photos will be detected
- detection - process of detection of chosen folder
- results - the folder will be opened with results

choose_folder()
---------------
This function allows user to choose path to folder, where are kept files to detection. As default takes path to photos of person with and without mask.

**Parameters**:

detect_path: str
   Global variable used to store default path to files that are going to be detected
folder_path: StringVar
   Used to choose concrete path to files that are going to be detected


detection_function()
--------------------
This function runs command to detect files from chosen folder. It uses already trained neural network called *best.pt*. After detection will be shown the information about it.

show_results()
--------------
This function allows user to see results of detection. As default it takes the path of latest created folder with results. It is possible to run on Windows and on MacOS.
