add_executable(project_executable source1.cpp source2.cpp)
target_include_directories(project_executable PUBLIC ${CMAKE_SOURCE_DIR}/include)
