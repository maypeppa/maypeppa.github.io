#ifndef __CRC32_CRC32_H__
#define __CRC32_CRC32_H__

uint32_t crc32_fast(const void* data, size_t length, uint32_t previousCrc32 = 0);

#endif // __CRC32_CRC32_H__
