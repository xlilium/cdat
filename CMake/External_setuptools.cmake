
set(setuptools_source "${CMAKE_CURRENT_BINARY_DIR}/build/setuptools")
set(setuptools_install "${cdat_EXTERNALS}")

configure_file(${cdat_CMAKE_SOURCE_DIR}/setuptools_make_step.cmake.in
  ${cdat_CMAKE_BINARY_DIR}/setuptools_make_step.cmake
  @ONLY)

configure_file(${cdat_CMAKE_SOURCE_DIR}/setuptools_install_step.cmake.in
  ${cdat_CMAKE_BINARY_DIR}/setuptools_install_step.cmake
  @ONLY)

set(setuptools_build_command ${CMAKE_COMMAND} -P ${cdat_CMAKE_BINARY_DIR}/setuptools_make_step.cmake)
set(setuptools_install_command ${CMAKE_COMMAND} -P ${cdat_CMAKE_BINARY_DIR}/setuptools_install_step.cmake)

ExternalProject_Add(setuptools
  DOWNLOAD_DIR ${CMAKE_CURRENT_BINARY_DIR}
  SOURCE_DIR ${setuptools_source}
  INSTALL_DIR ${setuptools_install}
  URL ${SETUPTOOLS_URL}/${SETUPTOOLS_GZ}
  URL_MD5 ${SETUPTOOLS_MD5}
  BUILD_IN_SOURCE 1
  PATCH_COMMAND ""
  CONFIGURE_COMMAND ""
  BUILD_COMMAND ${setuptools_build_command}
  INSTALL_COMMAND ${setuptools_install_command}
  DEPENDS ${setuptools_DEPENDENCIES}
  ${EP_LOG_OPTIONS}
)

set(setuptools_DIR "${setuptools_binary}" CACHE PATH "setuptools binary directory" FORCE)
mark_as_advanced(setuptools_DIR)
