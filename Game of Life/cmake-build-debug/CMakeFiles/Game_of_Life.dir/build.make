# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Game_of_Life.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Game_of_Life.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Game_of_Life.dir/flags.make

CMakeFiles/Game_of_Life.dir/main.c.o: CMakeFiles/Game_of_Life.dir/flags.make
CMakeFiles/Game_of_Life.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Game_of_Life.dir/main.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Game_of_Life.dir/main.c.o   -c "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/main.c"

CMakeFiles/Game_of_Life.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Game_of_Life.dir/main.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/main.c" > CMakeFiles/Game_of_Life.dir/main.c.i

CMakeFiles/Game_of_Life.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Game_of_Life.dir/main.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/main.c" -o CMakeFiles/Game_of_Life.dir/main.c.s

CMakeFiles/Game_of_Life.dir/main.c.o.requires:

.PHONY : CMakeFiles/Game_of_Life.dir/main.c.o.requires

CMakeFiles/Game_of_Life.dir/main.c.o.provides: CMakeFiles/Game_of_Life.dir/main.c.o.requires
	$(MAKE) -f CMakeFiles/Game_of_Life.dir/build.make CMakeFiles/Game_of_Life.dir/main.c.o.provides.build
.PHONY : CMakeFiles/Game_of_Life.dir/main.c.o.provides

CMakeFiles/Game_of_Life.dir/main.c.o.provides.build: CMakeFiles/Game_of_Life.dir/main.c.o


# Object files for target Game_of_Life
Game_of_Life_OBJECTS = \
"CMakeFiles/Game_of_Life.dir/main.c.o"

# External object files for target Game_of_Life
Game_of_Life_EXTERNAL_OBJECTS =

Game_of_Life: CMakeFiles/Game_of_Life.dir/main.c.o
Game_of_Life: CMakeFiles/Game_of_Life.dir/build.make
Game_of_Life: CMakeFiles/Game_of_Life.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Game_of_Life"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Game_of_Life.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Game_of_Life.dir/build: Game_of_Life

.PHONY : CMakeFiles/Game_of_Life.dir/build

CMakeFiles/Game_of_Life.dir/requires: CMakeFiles/Game_of_Life.dir/main.c.o.requires

.PHONY : CMakeFiles/Game_of_Life.dir/requires

CMakeFiles/Game_of_Life.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Game_of_Life.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Game_of_Life.dir/clean

CMakeFiles/Game_of_Life.dir/depend:
	cd "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life" "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life" "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug" "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug" "/Users/user/Desktop/School/Winter-2018/CIS-343/Github/CIS-343/Game of Life/cmake-build-debug/CMakeFiles/Game_of_Life.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Game_of_Life.dir/depend

