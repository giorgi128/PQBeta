#ifndef SSALLOC_H
#define SSALLOC_H

#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/time.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <sched.h>
#include <inttypes.h>
#include <string.h>

/* #define SSALLOC_USE_MALLOC */

#define SSALLOC_NUM_ALLOCATORS 4
#define SSALLOC_SIZE (1024LL * 1024 * 1024)

/* extern const size_t ssalloc_size_alloc[SSALLOC_NUM_ALLOCATORS]; */


void ssalloc_set(void* mem);
void ssalloc_init();
void ssalloc_align();
void ssalloc_align_alloc(unsigned int allocator);
void ssalloc_offset(size_t size);
void* ssalloc_alloc(unsigned int allocator, size_t size);
void ssfree_alloc(unsigned int allocator, void* ptr);
void* ssalloc(size_t size);
void ssfree(void* ptr);

#endif
