### aten.mm.default
|     | ATen Input Variations                                           | Status   | Isolated   |      PCC |   Host |
|----:|:----------------------------------------------------------------|:---------|:-----------|---------:|-------:|
|   0 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1024]> mat2 = ?    | Done     | Done       | 0.999968 |      0 |
|   1 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1280]> mat2 = ?    | Done     | Done       | 0.99997  |      0 |
|   2 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 1536]> mat2 = ?    | Done     | Done       | 0.999969 |      0 |
|   3 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 2048]> mat2 = ?    | Done     | Done       | 0.999968 |      0 |
|   4 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 512]> mat2 = ?     | Done     | Done       | 0.999966 |      0 |
|   5 | Tensor<[1, 1000]> self = ?,<br>Tensor<[1000, 768]> mat2 = ?     | Done     | Done       | 0.999971 |      0 |
|   6 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?    | Unknown  | Done       | 0.999964 |      0 |
|   7 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?    | Unknown  | Done       | 0.999966 |      0 |
|   8 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 32128]> mat2 = ?   | Unknown  | Done       | 0.999966 |      0 |
|   9 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?    | Unknown  | Done       | 0.999967 |      0 |
|  10 | Tensor<[1, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?     | Unknown  | Done       | 0.999968 |      0 |
|  11 | Tensor<[1, 10]> self = ?,<br>Tensor<[10, 128]> mat2 = ?         | Done     | Done       | 0.999995 |      0 |
|  12 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 64]> mat2 = ?        | Done     | Done       | 0.999982 |      0 |
|  13 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 784]> mat2 = ?       | Done     | Done       | 0.999976 |      0 |
|  14 | Tensor<[1, 128]> self = ?,<br>Tensor<[128, 9216]> mat2 = ?      | Done     | Done       | 0.999979 |      0 |
|  15 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 3]> mat2 = ?           | Done     | Done       | 0.999995 |      0 |
|  16 | Tensor<[1, 12]> self = ?,<br>Tensor<[12, 64]> mat2 = ?          | Done     | Done       | 0.999996 |      0 |
|  17 | Tensor<[1, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?     | Unknown  | Done       | 0.999954 |      0 |
|  18 | Tensor<[1, 21843]> self = ?,<br>Tensor<[21843, 768]> mat2 = ?   | Done     | Done       | 0.999466 |      0 |
|  19 | Tensor<[1, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?           | Done     | Done       | 0.999996 |      0 |
|  20 | Tensor<[1, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?     | Unknown  | Done       | 0.999943 |      0 |
|  21 | Tensor<[1, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?       | Unknown  | Done       | 0.999973 |      0 |
|  22 | Tensor<[1, 3]> self = ?,<br>Tensor<[3, 12]> mat2 = ?            | Done     | Done       | 0.999994 |      0 |
|  23 | Tensor<[1, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?    | Unknown  | Done       | 0.999927 |      0 |
|  24 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?      | Unknown  | Done       | 0.999972 |      0 |
|  25 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?      | Unknown  | Done       | 0.999971 |      0 |
|  26 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 32128]> mat2 = ?     | Unknown  | Done       | 0.999971 |      0 |
|  27 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?       | Unknown  | Done       | 0.999967 |      0 |
|  28 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?     | Unknown  | Done       | 0.999971 |      0 |
|  29 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Unknown  | Done       | 0.999973 |      0 |
|  30 | Tensor<[1, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?       | Done     | Done       | 0.99997  |      0 |
|  31 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 128]> mat2 = ?         | Done     | Done       | 0.99999  |      0 |
|  32 | Tensor<[1, 64]> self = ?,<br>Tensor<[64, 12]> mat2 = ?          | Done     | Done       | 0.99996  |      0 |
|  33 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?      | Unknown  | Done       | 0.999967 |      0 |
|  34 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 32128]> mat2 = ?     | Unknown  | Done       | 0.999968 |      0 |
|  35 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?     | Unknown  | Done       | 0.999968 |      0 |
|  36 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 512]> mat2 = ?       | Done     | Done       | 0.999969 |      0 |
|  37 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?     | Unknown  | Done       | 0.999969 |      0 |
|  38 | Tensor<[1, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.99997  |      0 |
|  39 | Tensor<[1, 784]> self = ?,<br>Tensor<[784, 128]> mat2 = ?       | Done     | Done       | 0.999971 |      0 |
|  40 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?   | Unknown  | Done       | 0.999966 |      0 |
|  41 | Tensor<[10, 1024]> self = ?,<br>Tensor<[1024, 4096]> mat2 = ?   | Unknown  | Done       | 0.999966 |      0 |
|  42 | Tensor<[10, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?          | Done     | Done       | 0.999995 |      0 |
|  43 | Tensor<[10, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?    | Unknown  | Done       | 0.999953 |      0 |
|  44 | Tensor<[10, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Unknown  | Done       | 0.999945 |      0 |
|  45 | Tensor<[10, 4096]> self = ?,<br>Tensor<[4096, 1024]> mat2 = ?   | Unknown  | Done       | 0.999934 |      0 |
|  46 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?     | Unknown  | Done       | 0.999971 |      0 |
|  47 | Tensor<[10, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?      | Unknown  | Done       | 0.999972 |      0 |
|  48 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Unknown  | Done       | 0.999968 |      0 |
|  49 | Tensor<[10, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Done       | 0.999969 |      0 |
|  50 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1024]> mat2 = ?       | Done     | Done       | 0.999992 |      0 |
|  51 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1280]> mat2 = ?       | Done     | Done       | 0.999992 |      0 |
|  52 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 1536]> mat2 = ?       | Done     | Done       | 0.999992 |      0 |
|  53 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 2048]> mat2 = ?       | Done     | Done       | 0.999992 |      0 |
|  54 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?        | Done     | Done       | 0.999992 |      0 |
|  55 | Tensor<[1000, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?        | Done     | Done       | 0.999992 |      0 |
|  56 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
|  57 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 256]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
|  58 | Tensor<[1024, 160]> self = ?,<br>Tensor<[160, 640]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
|  59 | Tensor<[1024, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
|  60 | Tensor<[1024, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?    | Done     | Done       | 0.999973 |      0 |
|  61 | Tensor<[1024, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?    | Done     | Done       | 0.999971 |      0 |
|  62 | Tensor<[1024, 640]> self = ?,<br>Tensor<[640, 160]> mat2 = ?    | Done     | Done       | 0.99997  |      0 |
|  63 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 3]> mat2 = ?            | Done     | Done       | 0.999995 |      0 |
|  64 | Tensor<[12, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?           | Done     | Done       | 0.999993 |      0 |
|  65 | Tensor<[128, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?  | Done     | Done       | 0.999798 |      0 |
|  66 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 64]> mat2 = ?          | Done     | Done       | 0.999992 |      0 |
|  67 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 784]> mat2 = ?         | Done     | Done       | 0.999993 |      0 |
|  68 | Tensor<[128, 1]> self = ?,<br>Tensor<[1, 9216]> mat2 = ?        | Done     | Done       | 0.999992 |      0 |
|  69 | Tensor<[14, 2048]> self = ?,<br>Tensor<[2048, 512]> mat2 = ?    | Done     | Done       | 0.999956 |      0 |
|  70 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 2048]> mat2 = ?     | Done     | Done       | 0.999972 |      0 |
|  71 | Tensor<[14, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?      | Done     | Done       | 0.999971 |      0 |
|  72 | Tensor<[15, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Unknown  | Done       | 0.999964 |      0 |
|  73 | Tensor<[15, 384]> self = ?,<br>Tensor<[384, 512]> mat2 = ?      | Unknown  | Done       | 0.999973 |      0 |
|  74 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?     | Unknown  | Done       | 0.999971 |      0 |
|  75 | Tensor<[15, 512]> self = ?,<br>Tensor<[512, 384]> mat2 = ?      | Unknown  | Done       | 0.999972 |      0 |
|  76 | Tensor<[1500, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?    | Unknown  | Done       | 0.999963 |      0 |
|  77 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?   | Done     | Done       | 0.999954 |      0 |
|  78 | Tensor<[160, 1024]> self = ?,<br>Tensor<[1024, 640]> mat2 = ?   | Done     | Done       | 0.999966 |      0 |
|  79 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
|  80 | Tensor<[160, 256]> self = ?,<br>Tensor<[256, 160]> mat2 = ?     | Done     | Done       | 0.999979 |      0 |
|  81 | Tensor<[16384, 128]> self = ?,<br>Tensor<[128, 32]> mat2 = ?    | Done     | Done       | 0.99998  |      0 |
|  82 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 128]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
|  83 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 256]> mat2 = ?     | Done     | Done       | 0.999989 |      0 |
|  84 | Tensor<[16384, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?      | Done     | Done       | 0.999989 |      0 |
|  85 | Tensor<[196, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
|  86 | Tensor<[196, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?   | Done     | Done       | 0.999944 |      0 |
|  87 | Tensor<[196, 384]> self = ?,<br>Tensor<[384, 768]> mat2 = ?     | Done     | Done       | 0.999973 |      0 |
|  88 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Done     | Done       | 0.999968 |      0 |
|  89 | Tensor<[196, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?     | Done     | Done       | 0.999963 |      0 |
|  90 | Tensor<[197, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?   | Done     | Done       | 0.999944 |      0 |
|  91 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?    | Done     | Done       | 0.999968 |      0 |
|  92 | Tensor<[197, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?     | Done     | Done       | 0.999968 |      0 |
|  93 | Tensor<[2, 1]> self = ?,<br>Tensor<[1, 512]> mat2 = ?           | Done     | Done       | 0.999997 |      0 |
|  94 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 1]> mat2 = ?         | Done     | Done       | 1        |      0 |
|  95 | Tensor<[2, 512]> self = ?,<br>Tensor<[512, 512]> mat2 = ?       | Done     | Done       | 0.99997  |      0 |
|  96 | Tensor<[2048, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?      | Done     | Done       | 0.999992 |      0 |
|  97 | Tensor<[2048, 768]> self = ?,<br>Tensor<[768, 262]> mat2 = ?    | Removed  | Done       | 0.999968 |      0 |
|  98 | Tensor<[21843, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?       | Done     | Done       | 0.999992 |      0 |
|  99 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 12]> mat2 = ?      | Removed  | Done       | 0.99997  |      0 |
| 100 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 16]> mat2 = ?      | Removed  | Done       | 0.99997  |      0 |
| 101 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 24]> mat2 = ?      | Removed  | Done       | 0.99997  |      0 |
| 102 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 32]> mat2 = ?      | Removed  | Done       | 0.999971 |      0 |
| 103 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 3]> mat2 = ?       | Removed  | Done       | 0.99997  |      0 |
| 104 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 4]> mat2 = ?       | Removed  | Done       | 0.999971 |      0 |
| 105 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 6]> mat2 = ?       | Removed  | Done       | 0.99997  |      0 |
| 106 | Tensor<[225, 512]> self = ?,<br>Tensor<[512, 8]> mat2 = ?       | Removed  | Done       | 0.999972 |      0 |
| 107 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
| 108 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 256]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
| 109 | Tensor<[256, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
| 110 | Tensor<[256, 160]> self = ?,<br>Tensor<[160, 160]> mat2 = ?     | Done     | Done       | 0.999982 |      0 |
| 111 | Tensor<[256, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?  | Done     | Done       | 0.999806 |      0 |
| 112 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 1024]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
| 113 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Done     | Done       | 0.999979 |      0 |
| 114 | Tensor<[256, 256]> self = ?,<br>Tensor<[256, 512]> mat2 = ?     | Done     | Done       | 0.999979 |      0 |
| 115 | Tensor<[256, 32]> self = ?,<br>Tensor<[32, 32]> mat2 = ?        | Done     | Done       | 0.99999  |      0 |
| 116 | Tensor<[256, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?    | Done     | Done       | 0.999846 |      0 |
| 117 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?     | Done     | Done       | 0.999971 |      0 |
| 118 | Tensor<[256, 512]> self = ?,<br>Tensor<[512, 768]> mat2 = ?     | Done     | Done       | 0.999972 |      0 |
| 119 | Tensor<[256, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?        | Done     | Done       | 0.999987 |      0 |
| 120 | Tensor<[256, 768]> self = ?,<br>Tensor<[768, 384]> mat2 = ?     | Done     | Done       | 0.999963 |      0 |
| 121 | Tensor<[3, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?            | Done     | Done       | 0.999999 |      0 |
| 122 | Tensor<[3072, 196]> self = ?,<br>Tensor<[196, 768]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
| 123 | Tensor<[3072, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
| 124 | Tensor<[3072, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?      | Done     | Done       | 0.999986 |      0 |
| 125 | Tensor<[32, 1536]> self = ?,<br>Tensor<[1536, 250880]> mat2 = ? | Done     | Done       | 0.99996  |      0 |
| 126 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 128]> mat2 = ?  | Done     | Done       | 0.999798 |      0 |
| 127 | Tensor<[32, 16384]> self = ?,<br>Tensor<[16384, 32]> mat2 = ?   | Done     | Done       | 0.999791 |      0 |
| 128 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 16384]> mat2 = ?    | Done     | Done       | 0.999975 |      0 |
| 129 | Tensor<[32, 256]> self = ?,<br>Tensor<[256, 32]> mat2 = ?       | Done     | Done       | 0.999978 |      0 |
| 130 | Tensor<[384, 768]> self = ?,<br>Tensor<[768, 196]> mat2 = ?     | Done     | Done       | 0.999964 |      0 |
| 131 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 51865]> mat2 = ?     | Unknown  | Done       | 0.999968 |      0 |
| 132 | Tensor<[4, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?       | Unknown  | Done       | 0.999968 |      0 |
| 133 | Tensor<[4096, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?     | Done     | Done       | 0.999975 |      0 |
| 134 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 256]> mat2 = ?      | Done     | Done       | 0.999986 |      0 |
| 135 | Tensor<[4096, 64]> self = ?,<br>Tensor<[64, 64]> mat2 = ?       | Done     | Done       | 0.999986 |      0 |
| 136 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 50257]> mat2 = ?    | Unknown  | Done       | 0.999968 |      0 |
| 137 | Tensor<[45, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Unknown  | Done       | 0.999968 |      0 |
| 138 | Tensor<[49, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?    | Done     | Done       | 0.999961 |      0 |
| 139 | Tensor<[49, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
| 140 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 1024]> mat2 = ?    | Unknown  | Done       | 0.999966 |      0 |
| 141 | Tensor<[5, 1024]> self = ?,<br>Tensor<[1024, 3072]> mat2 = ?    | Unknown  | Done       | 0.999966 |      0 |
| 142 | Tensor<[50, 3072]> self = ?,<br>Tensor<[3072, 768]> mat2 = ?    | Done     | Done       | 0.999945 |      0 |
| 143 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 3072]> mat2 = ?     | Done     | Done       | 0.999969 |      0 |
| 144 | Tensor<[50, 768]> self = ?,<br>Tensor<[768, 768]> mat2 = ?      | Done     | Done       | 0.999969 |      0 |
| 145 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 2048]> mat2 = ?      | Done     | Done       | 0.999992 |      0 |
| 146 | Tensor<[512, 14]> self = ?,<br>Tensor<[14, 512]> mat2 = ?       | Done     | Done       | 0.999991 |      0 |
| 147 | Tensor<[512, 1]> self = ?,<br>Tensor<[1, 768]> mat2 = ?         | Done     | Done       | 0.999992 |      0 |
| 148 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Done     | Done       | 0.999979 |      0 |
| 149 | Tensor<[512, 256]> self = ?,<br>Tensor<[256, 768]> mat2 = ?     | Done     | Done       | 0.999976 |      0 |
| 150 | Tensor<[512, 2]> self = ?,<br>Tensor<[2, 512]> mat2 = ?         | Done     | Done       | 0.999992 |      0 |
| 151 | Tensor<[59, 1024]> self = ?,<br>Tensor<[1024, 512]> mat2 = ?    | Unknown  | Done       | 0.999955 |      0 |
| 152 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 1024]> mat2 = ?     | Unknown  | Done       | 0.999971 |      0 |
| 153 | Tensor<[59, 512]> self = ?,<br>Tensor<[512, 50272]> mat2 = ?    | Unknown  | Done       | 0.999971 |      0 |
| 154 | Tensor<[64, 1536]> self = ?,<br>Tensor<[1536, 768]> mat2 = ?    | Done     | Done       | 0.99996  |      0 |
| 155 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?          | Done     | Done       | 0.999994 |      0 |
| 156 | Tensor<[64, 1]> self = ?,<br>Tensor<[1, 12]> mat2 = ?           | Done     | Done       | 0.999992 |      0 |
| 157 | Tensor<[64, 2048]> self = ?,<br>Tensor<[2048, 1024]> mat2 = ?   | Done     | Done       | 0.999955 |      0 |
| 158 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 4096]> mat2 = ?     | Done     | Done       | 0.999976 |      0 |
| 159 | Tensor<[64, 256]> self = ?,<br>Tensor<[256, 64]> mat2 = ?       | Done     | Done       | 0.999979 |      0 |
| 160 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 256]> mat2 = ?    | Done     | Done       | 0.999843 |      0 |
| 161 | Tensor<[64, 4096]> self = ?,<br>Tensor<[4096, 64]> mat2 = ?     | Done     | Done       | 0.999853 |      0 |
| 162 | Tensor<[640, 1024]> self = ?,<br>Tensor<[1024, 160]> mat2 = ?   | Done     | Done       | 0.999966 |      0 |
| 163 | Tensor<[7, 768]> self = ?,<br>Tensor<[768, 2]> mat2 = ?         | Done     | Done       | 0.99999  |      0 |
| 164 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 3072]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
| 165 | Tensor<[768, 196]> self = ?,<br>Tensor<[196, 384]> mat2 = ?     | Done     | Done       | 0.999982 |      0 |
| 166 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 3072]> mat2 = ?    | Done     | Done       | 0.999982 |      0 |
| 167 | Tensor<[768, 197]> self = ?,<br>Tensor<[197, 768]> mat2 = ?     | Done     | Done       | 0.999982 |      0 |
| 168 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 3072]> mat2 = ?      | Done     | Done       | 0.999986 |      0 |
| 169 | Tensor<[768, 50]> self = ?,<br>Tensor<[50, 768]> mat2 = ?       | Done     | Done       | 0.999986 |      0 |
| 170 | Tensor<[784, 1]> self = ?,<br>Tensor<[1, 128]> mat2 = ?         | Done     | Done       | 0.999992 |      0 |
| 171 | Tensor<[784, 384]> self = ?,<br>Tensor<[384, 192]> mat2 = ?     | Done     | Done       | 0.999973 |      0 |
| 172 | Tensor<[784, 512]> self = ?,<br>Tensor<[512, 256]> mat2 = ?     | Done     | Done       | 0.999971 |      0 |
| 173 | Tensor<[920, 256]> self = ?,<br>Tensor<[256, 256]> mat2 = ?     | Done     | Done       | 0.999975 |      0 |

