cmake_minimum_required(VERSION 3.21)
project(my_project_name
  VERSION 0.0.1
  LANGUAGES CXX
)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# add_executable(project_executable source1.cpp source2.cpp)
add_subdirectory(source)
# add_subdirectory(test)
