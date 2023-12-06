#ifndef _PCH_H_
#define _PCH_H_

/// pch.h: This is a precompiled header file.
/// Files listed below are compiled only once, improving build performance for future builds.
/// This also affects IntelliSense performance, including code completion and many code browsing features.
/// However, files listed here are ALL re-compiled if any one of them is updated between builds.
/// Do not add files here that you will be updating frequently as this negates the performance advantage.

#define WIN32_LEAN_AND_MEAN             // Exclude rarely-used stuff from Windows headers

#include <Windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <sal.h>
#include <string>
#include <string.h>
#include <sstream>
#include <fstream>

#include <BS_thread_pool_light.hpp>

#endif//_PCH_H_