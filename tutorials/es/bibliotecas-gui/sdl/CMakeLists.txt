project(qt-sdl)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_library(sdlqtexample
  src/Area.cpp
  src/SdlImage.cpp
  src/SdlWindow.cpp
)

message("Headers generados: ${UIS_HEADERS}")
# Agrego la carpeta con los headers autogenerados a los includes
message("Agregando '${PROJECT_BINARY_DIR}' como directorio de includes")
include_directories(${PROJECT_BINARY_DIR})

add_executable (sdl-demo
  src/mainSDL.cpp  
)


target_link_libraries(sdl-demo sdlqtexample SDL2 SDL2_image)

install(FILES assets/cat.gif DESTINATION ${CMAKE_BINARY_DIR})
