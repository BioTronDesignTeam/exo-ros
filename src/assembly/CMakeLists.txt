cmake_minimum_required(VERSION 3.20)

project(assembly)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  urdf
  config
  meshes
  DESTINATION share/${PROJECT_NAME}
)

ament_package()