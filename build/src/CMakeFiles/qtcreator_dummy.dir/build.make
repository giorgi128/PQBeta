# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dan/DijkstraNew/kpqueue

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dan/DijkstraNew/kpqueue/build

# Include any dependencies generated for this target.
include src/CMakeFiles/qtcreator_dummy.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/qtcreator_dummy.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/qtcreator_dummy.dir/flags.make

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o: src/CMakeFiles/qtcreator_dummy.dir/flags.make
src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o: ../src/util/thread_local_ptr.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/dan/DijkstraNew/kpqueue/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o"
	cd /home/dan/DijkstraNew/kpqueue/build/src && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o -c /home/dan/DijkstraNew/kpqueue/src/util/thread_local_ptr.cpp

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.i"
	cd /home/dan/DijkstraNew/kpqueue/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/dan/DijkstraNew/kpqueue/src/util/thread_local_ptr.cpp > CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.i

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.s"
	cd /home/dan/DijkstraNew/kpqueue/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/dan/DijkstraNew/kpqueue/src/util/thread_local_ptr.cpp -o CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.s

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.requires:
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.requires

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.provides: src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.requires
	$(MAKE) -f src/CMakeFiles/qtcreator_dummy.dir/build.make src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.provides.build
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.provides

src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.provides.build: src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o

# Object files for target qtcreator_dummy
qtcreator_dummy_OBJECTS = \
"CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o"

# External object files for target qtcreator_dummy
qtcreator_dummy_EXTERNAL_OBJECTS =

src/libqtcreator_dummy.a: src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o
src/libqtcreator_dummy.a: src/CMakeFiles/qtcreator_dummy.dir/build.make
src/libqtcreator_dummy.a: src/CMakeFiles/qtcreator_dummy.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX static library libqtcreator_dummy.a"
	cd /home/dan/DijkstraNew/kpqueue/build/src && $(CMAKE_COMMAND) -P CMakeFiles/qtcreator_dummy.dir/cmake_clean_target.cmake
	cd /home/dan/DijkstraNew/kpqueue/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/qtcreator_dummy.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/qtcreator_dummy.dir/build: src/libqtcreator_dummy.a
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/build

src/CMakeFiles/qtcreator_dummy.dir/requires: src/CMakeFiles/qtcreator_dummy.dir/util/thread_local_ptr.cpp.o.requires
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/requires

src/CMakeFiles/qtcreator_dummy.dir/clean:
	cd /home/dan/DijkstraNew/kpqueue/build/src && $(CMAKE_COMMAND) -P CMakeFiles/qtcreator_dummy.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/clean

src/CMakeFiles/qtcreator_dummy.dir/depend:
	cd /home/dan/DijkstraNew/kpqueue/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dan/DijkstraNew/kpqueue /home/dan/DijkstraNew/kpqueue/src /home/dan/DijkstraNew/kpqueue/build /home/dan/DijkstraNew/kpqueue/build/src /home/dan/DijkstraNew/kpqueue/build/src/CMakeFiles/qtcreator_dummy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/qtcreator_dummy.dir/depend

