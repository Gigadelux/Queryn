python3 adapter_model_training.py
20:18:45 [INFO] Device: mps  |  Pairs: 56  |  Epochs: 15  |  Batch: 128
20:18:45 [INFO]
─── [1/56] ada-002 → te3-small ───
11:12:38 [INFO] [ada-002_to_te3-small] 1536d → 1536d  hidden=1536
11:13:01 [INFO] [ada-002_to_te3-small] 01/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.8022
11:13:23 [INFO] [ada-002_to_te3-small] 02/15  train_loss=0.00007  test_loss=0.00011  test_cos=0.8111
11:13:44 [INFO] [ada-002_to_te3-small] 03/15  train_loss=0.00007  test_loss=0.00011  test_cos=0.8229
11:14:05 [INFO] [ada-002_to_te3-small] 04/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.8296
11:14:27 [INFO] [ada-002_to_te3-small] 05/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.8327
11:14:48 [INFO] [ada-002_to_te3-small] 06/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8352
11:15:09 [INFO] [ada-002_to_te3-small] 07/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8364
11:15:31 [INFO] [ada-002_to_te3-small] 08/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8378
11:15:52 [INFO] [ada-002_to_te3-small] 09/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8386
11:16:14 [INFO] [ada-002_to_te3-small] 10/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8392
11:16:35 [INFO] [ada-002_to_te3-small] 11/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8403
11:16:56 [INFO] [ada-002_to_te3-small] 12/15  train_loss=0.00006  test_loss=0.00010  test_cos=0.8412
11:17:18 [INFO] [ada-002_to_te3-small] 13/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.8417
11:17:39 [INFO] [ada-002_to_te3-small] 14/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.8423
11:18:00 [INFO] [ada-002_to_te3-small] 15/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.8425
11:18:00 [INFO] [ada-002_to_te3-small] saved → ada-002_to_te3-small.pt  (321.7s)
─── [2/56] ada-002 → qwen3-emb-8b ───
20:18:45 [INFO] [ada-002_to_qwen3-emb-8b] 1536d → 4096d  hidden=2048
20:19:41 [INFO] [ada-002_to_qwen3-emb-8b] 01/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.7162
20:20:37 [INFO] [ada-002_to_qwen3-emb-8b] 02/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.7373
20:21:32 [INFO] [ada-002_to_qwen3-emb-8b] 03/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7448
20:22:28 [INFO] [ada-002_to_qwen3-emb-8b] 04/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7486
20:23:24 [INFO] [ada-002_to_qwen3-emb-8b] 05/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7510
20:24:20 [INFO] [ada-002_to_qwen3-emb-8b] 06/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7533
20:25:16 [INFO] [ada-002_to_qwen3-emb-8b] 07/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7545
20:26:12 [INFO] [ada-002_to_qwen3-emb-8b] 08/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7551
20:27:10 [INFO] [ada-002_to_qwen3-emb-8b] 09/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7544
20:28:10 [INFO] [ada-002_to_qwen3-emb-8b] 10/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7570
20:29:11 [INFO] [ada-002_to_qwen3-emb-8b] 11/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7584
20:30:12 [INFO] [ada-002_to_qwen3-emb-8b] 12/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7587
20:31:19 [INFO] [ada-002_to_qwen3-emb-8b] 13/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7596
20:32:26 [INFO] [ada-002_to_qwen3-emb-8b] 14/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7605
20:33:28 [INFO] [ada-002_to_qwen3-emb-8b] 15/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7615
20:33:29 [INFO] [ada-002_to_qwen3-emb-8b] saved → ada-002_to_qwen3-emb-8b.pt  (883.9s)
20:33:29 [INFO]
─── [3/56] ada-002 → bge-m3 ───
20:33:29 [INFO] [ada-002_to_bge-m3] 1536d → 1024d  hidden=1536
20:33:51 [INFO] [ada-002_to_bge-m3] 01/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.8176
20:34:12 [INFO] [ada-002_to_bge-m3] 02/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8243
20:34:33 [INFO] [ada-002_to_bge-m3] 03/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8302
20:34:54 [INFO] [ada-002_to_bge-m3] 04/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8342
20:35:15 [INFO] [ada-002_to_bge-m3] 05/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8366
20:35:36 [INFO] [ada-002_to_bge-m3] 06/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8381
20:35:57 [INFO] [ada-002_to_bge-m3] 07/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8386
20:36:19 [INFO] [ada-002_to_bge-m3] 08/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8391
20:36:40 [INFO] [ada-002_to_bge-m3] 09/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8401
20:37:01 [INFO] [ada-002_to_bge-m3] 10/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8409
20:37:23 [INFO] [ada-002_to_bge-m3] 11/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8414
20:37:44 [INFO] [ada-002_to_bge-m3] 12/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8420
20:38:05 [INFO] [ada-002_to_bge-m3] 13/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8426
20:38:28 [INFO] [ada-002_to_bge-m3] 14/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8425
20:38:50 [INFO] [ada-002_to_bge-m3] 15/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.8433
20:38:50 [INFO] [ada-002_to_bge-m3] saved → ada-002_to_bge-m3.pt  (321.4s)
20:38:50 [INFO]
─── [4/56] ada-002 → me5-large ───
20:38:50 [INFO] [ada-002_to_me5-large] 1536d → 1024d  hidden=1536
20:39:13 [INFO] [ada-002_to_me5-large] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9225
20:39:35 [INFO] [ada-002_to_me5-large] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9261
20:39:57 [INFO] [ada-002_to_me5-large] 03/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9272
20:40:19 [INFO] [ada-002_to_me5-large] 04/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9296
20:40:40 [INFO] [ada-002_to_me5-large] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9304
20:41:01 [INFO] [ada-002_to_me5-large] 06/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9317
20:41:23 [INFO] [ada-002_to_me5-large] 07/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9321
20:41:44 [INFO] [ada-002_to_me5-large] 08/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9326
20:42:05 [INFO] [ada-002_to_me5-large] 09/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9328
20:42:27 [INFO] [ada-002_to_me5-large] 10/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9330
20:42:48 [INFO] [ada-002_to_me5-large] 11/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9333
20:43:09 [INFO] [ada-002_to_me5-large] 12/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9334
20:43:31 [INFO] [ada-002_to_me5-large] 13/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9336
20:43:52 [INFO] [ada-002_to_me5-large] 14/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9337
20:44:13 [INFO] [ada-002_to_me5-large] 15/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9339
20:44:14 [INFO] [ada-002_to_me5-large] saved → ada-002_to_me5-large.pt  (323.5s)
20:44:14 [INFO]
─── [5/56] ada-002 → pplx-embed-1 ───
20:44:14 [INFO] [ada-002_to_pplx-embed-1] 1536d → 1024d  hidden=1536
20:44:35 [INFO] [ada-002_to_pplx-embed-1] 01/15  train_loss=0.00375  test_loss=0.00547  test_cos=0.6560
20:44:56 [INFO] [ada-002_to_pplx-embed-1] 02/15  train_loss=0.00322  test_loss=0.00512  test_cos=0.6821
20:45:18 [INFO] [ada-002_to_pplx-embed-1] 03/15  train_loss=0.00314  test_loss=0.00498  test_cos=0.6916
20:45:39 [INFO] [ada-002_to_pplx-embed-1] 04/15  train_loss=0.00309  test_loss=0.00488  test_cos=0.6996
20:46:01 [INFO] [ada-002_to_pplx-embed-1] 05/15  train_loss=0.00307  test_loss=0.00480  test_cos=0.7048
20:46:24 [INFO] [ada-002_to_pplx-embed-1] 06/15  train_loss=0.00305  test_loss=0.00473  test_cos=0.7098
20:46:47 [INFO] [ada-002_to_pplx-embed-1] 07/15  train_loss=0.00303  test_loss=0.00467  test_cos=0.7139
20:47:09 [INFO] [ada-002_to_pplx-embed-1] 08/15  train_loss=0.00301  test_loss=0.00462  test_cos=0.7167
20:47:30 [INFO] [ada-002_to_pplx-embed-1] 09/15  train_loss=0.00300  test_loss=0.00459  test_cos=0.7188
20:47:52 [INFO] [ada-002_to_pplx-embed-1] 10/15  train_loss=0.00299  test_loss=0.00456  test_cos=0.7206
20:48:13 [INFO] [ada-002_to_pplx-embed-1] 11/15  train_loss=0.00298  test_loss=0.00453  test_cos=0.7226
20:48:34 [INFO] [ada-002_to_pplx-embed-1] 12/15  train_loss=0.00297  test_loss=0.00450  test_cos=0.7248
20:48:55 [INFO] [ada-002_to_pplx-embed-1] 13/15  train_loss=0.00296  test_loss=0.00448  test_cos=0.7263
20:49:16 [INFO] [ada-002_to_pplx-embed-1] 14/15  train_loss=0.00295  test_loss=0.00446  test_cos=0.7273
20:49:38 [INFO] [ada-002_to_pplx-embed-1] 15/15  train_loss=0.00294  test_loss=0.00443  test_cos=0.7293
20:49:38 [INFO] [ada-002_to_pplx-embed-1] saved → ada-002_to_pplx-embed-1.pt  (324.2s)
20:49:38 [INFO]
─── [6/56] ada-002 → nemotron-1b-free ───
20:49:38 [INFO] [ada-002_to_nemotron-1b-free] 1536d → 2048d  hidden=2048
20:50:19 [INFO] [ada-002_to_nemotron-1b-free] 01/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.6341
20:50:59 [INFO] [ada-002_to_nemotron-1b-free] 02/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6441
20:51:39 [INFO] [ada-002_to_nemotron-1b-free] 03/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6507
20:52:23 [INFO] [ada-002_to_nemotron-1b-free] 04/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6668
20:53:04 [INFO] [ada-002_to_nemotron-1b-free] 05/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6685
20:53:45 [INFO] [ada-002_to_nemotron-1b-free] 06/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6742
20:54:26 [INFO] [ada-002_to_nemotron-1b-free] 07/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6770
20:55:08 [INFO] [ada-002_to_nemotron-1b-free] 08/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6792
20:55:48 [INFO] [ada-002_to_nemotron-1b-free] 09/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6800
20:56:27 [INFO] [ada-002_to_nemotron-1b-free] 10/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6805
20:57:06 [INFO] [ada-002_to_nemotron-1b-free] 11/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6806
20:57:45 [INFO] [ada-002_to_nemotron-1b-free] 12/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6809
20:58:24 [INFO] [ada-002_to_nemotron-1b-free] 13/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6810
20:59:04 [INFO] [ada-002_to_nemotron-1b-free] 14/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6821
20:59:43 [INFO] [ada-002_to_nemotron-1b-free] 15/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.6828
20:59:43 [INFO] [ada-002_to_nemotron-1b-free] saved → ada-002_to_nemotron-1b-free.pt  (604.9s)
20:59:43 [INFO]
─── [7/56] ada-002 → fastembed-bge-small ───
20:59:43 [INFO] [ada-002_to_fastembed-bge-small] 1536d → 384d  hidden=1536
20:59:59 [INFO] [ada-002_to_fastembed-bge-small] 01/15  train_loss=0.00020  test_loss=0.00035  test_cos=0.8543
21:00:15 [INFO] [ada-002_to_fastembed-bge-small] 02/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8631
21:00:31 [INFO] [ada-002_to_fastembed-bge-small] 03/15  train_loss=0.00018  test_loss=0.00032  test_cos=0.8680
21:00:47 [INFO] [ada-002_to_fastembed-bge-small] 04/15  train_loss=0.00018  test_loss=0.00031  test_cos=0.8719
21:01:03 [INFO] [ada-002_to_fastembed-bge-small] 05/15  train_loss=0.00018  test_loss=0.00031  test_cos=0.8732
21:01:19 [INFO] [ada-002_to_fastembed-bge-small] 06/15  train_loss=0.00018  test_loss=0.00031  test_cos=0.8753
21:01:35 [INFO] [ada-002_to_fastembed-bge-small] 07/15  train_loss=0.00018  test_loss=0.00030  test_cos=0.8758
21:01:51 [INFO] [ada-002_to_fastembed-bge-small] 08/15  train_loss=0.00018  test_loss=0.00030  test_cos=0.8781
21:02:06 [INFO] [ada-002_to_fastembed-bge-small] 09/15  train_loss=0.00018  test_loss=0.00030  test_cos=0.8785
21:02:22 [INFO] [ada-002_to_fastembed-bge-small] 10/15  train_loss=0.00017  test_loss=0.00030  test_cos=0.8791
21:02:38 [INFO] [ada-002_to_fastembed-bge-small] 11/15  train_loss=0.00017  test_loss=0.00030  test_cos=0.8796
21:02:54 [INFO] [ada-002_to_fastembed-bge-small] 12/15  train_loss=0.00017  test_loss=0.00030  test_cos=0.8795
21:03:10 [INFO] [ada-002_to_fastembed-bge-small] 13/15  train_loss=0.00017  test_loss=0.00029  test_cos=0.8801
21:03:26 [INFO] [ada-002_to_fastembed-bge-small] 14/15  train_loss=0.00017  test_loss=0.00029  test_cos=0.8806
21:03:42 [INFO] [ada-002_to_fastembed-bge-small] 15/15  train_loss=0.00017  test_loss=0.00029  test_cos=0.8808
21:03:42 [INFO] [ada-002_to_fastembed-bge-small] saved → ada-002_to_fastembed-bge-small.pt  (238.7s)
21:03:42 [INFO]
─── [8/56] te3-small → ada-002 ───
21:03:42 [INFO] [te3-small_to_ada-002] 1536d → 1536d  hidden=1536
21:04:07 [INFO] [te3-small_to_ada-002] 01/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9370
21:04:31 [INFO] [te3-small_to_ada-002] 02/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9392
21:04:56 [INFO] [te3-small_to_ada-002] 03/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9398
21:05:21 [INFO] [te3-small_to_ada-002] 04/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9412
21:05:46 [INFO] [te3-small_to_ada-002] 05/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9419
21:06:11 [INFO] [te3-small_to_ada-002] 06/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9428
21:06:36 [INFO] [te3-small_to_ada-002] 07/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9440
21:07:01 [INFO] [te3-small_to_ada-002] 08/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9446
21:07:26 [INFO] [te3-small_to_ada-002] 09/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9451
21:07:51 [INFO] [te3-small_to_ada-002] 10/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9455
21:08:16 [INFO] [te3-small_to_ada-002] 11/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9459
21:08:41 [INFO] [te3-small_to_ada-002] 12/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9462
21:09:05 [INFO] [te3-small_to_ada-002] 13/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9463
21:09:30 [INFO] [te3-small_to_ada-002] 14/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9464
21:09:55 [INFO] [te3-small_to_ada-002] 15/15  train_loss=0.00002  test_loss=0.00003  test_cos=0.9465
21:09:55 [INFO] [te3-small_to_ada-002] saved → te3-small_to_ada-002.pt  (373.5s)
21:09:55 [INFO]
─── [9/56] te3-small → qwen3-emb-8b ───
21:09:55 [INFO] [te3-small_to_qwen3-emb-8b] 1536d → 4096d  hidden=2048
21:10:59 [INFO] [te3-small_to_qwen3-emb-8b] 01/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6992
21:12:03 [INFO] [te3-small_to_qwen3-emb-8b] 02/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7186
21:13:07 [INFO] [te3-small_to_qwen3-emb-8b] 03/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7221
21:14:10 [INFO] [te3-small_to_qwen3-emb-8b] 04/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7197
21:15:14 [INFO] [te3-small_to_qwen3-emb-8b] 05/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7212
21:16:17 [INFO] [te3-small_to_qwen3-emb-8b] 06/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7254
21:17:21 [INFO] [te3-small_to_qwen3-emb-8b] 07/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7337
21:18:25 [INFO] [te3-small_to_qwen3-emb-8b] 08/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.7395
21:19:29 [INFO] [te3-small_to_qwen3-emb-8b] 09/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7435
21:20:33 [INFO] [te3-small_to_qwen3-emb-8b] 10/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7462
21:21:38 [INFO] [te3-small_to_qwen3-emb-8b] 11/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7479
21:22:42 [INFO] [te3-small_to_qwen3-emb-8b] 12/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7490
21:23:46 [INFO] [te3-small_to_qwen3-emb-8b] 13/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7499
21:24:50 [INFO] [te3-small_to_qwen3-emb-8b] 14/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7509
21:25:54 [INFO] [te3-small_to_qwen3-emb-8b] 15/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7516
21:25:54 [INFO] [te3-small_to_qwen3-emb-8b] saved → te3-small_to_qwen3-emb-8b.pt  (959.0s)
21:25:54 [INFO]
─── [10/56] te3-small → bge-m3 ───
21:25:54 [INFO] [te3-small_to_bge-m3] 1536d → 1024d  hidden=1536
21:26:15 [INFO] [te3-small_to_bge-m3] 01/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.8077
21:26:36 [INFO] [te3-small_to_bge-m3] 02/15  train_loss=0.00011  test_loss=0.00017  test_cos=0.8103
21:26:57 [INFO] [te3-small_to_bge-m3] 03/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8150
21:27:18 [INFO] [te3-small_to_bge-m3] 04/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8173
21:27:38 [INFO] [te3-small_to_bge-m3] 05/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8200
21:27:59 [INFO] [te3-small_to_bge-m3] 06/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8221
21:28:20 [INFO] [te3-small_to_bge-m3] 07/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8231
21:28:41 [INFO] [te3-small_to_bge-m3] 08/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8241
21:29:01 [INFO] [te3-small_to_bge-m3] 09/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8252
21:29:22 [INFO] [te3-small_to_bge-m3] 10/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8258
21:29:43 [INFO] [te3-small_to_bge-m3] 11/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8267
21:30:04 [INFO] [te3-small_to_bge-m3] 12/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8274
21:30:25 [INFO] [te3-small_to_bge-m3] 13/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8281
21:30:45 [INFO] [te3-small_to_bge-m3] 14/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8282
21:31:06 [INFO] [te3-small_to_bge-m3] 15/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.8288
21:31:06 [INFO] [te3-small_to_bge-m3] saved → te3-small_to_bge-m3.pt  (312.1s)
21:31:06 [INFO]
─── [11/56] te3-small → me5-large ───
21:31:06 [INFO] [te3-small_to_me5-large] 1536d → 1024d  hidden=1536
21:31:28 [INFO] [te3-small_to_me5-large] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9205
21:31:49 [INFO] [te3-small_to_me5-large] 02/15  train_loss=0.00004  test_loss=0.00008  test_cos=0.9195
21:32:10 [INFO] [te3-small_to_me5-large] 03/15  train_loss=0.00004  test_loss=0.00008  test_cos=0.9194
21:32:31 [INFO] [te3-small_to_me5-large] 04/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9222
21:32:52 [INFO] [te3-small_to_me5-large] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9237
21:33:13 [INFO] [te3-small_to_me5-large] 06/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9248
21:33:33 [INFO] [te3-small_to_me5-large] 07/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9247
21:33:54 [INFO] [te3-small_to_me5-large] 08/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9254
21:34:15 [INFO] [te3-small_to_me5-large] 09/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9259
21:34:36 [INFO] [te3-small_to_me5-large] 10/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9260
21:34:56 [INFO] [te3-small_to_me5-large] 11/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9265
21:35:17 [INFO] [te3-small_to_me5-large] 12/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9261
21:35:38 [INFO] [te3-small_to_me5-large] 13/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9263
21:35:58 [INFO] [te3-small_to_me5-large] 14/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9266
21:36:19 [INFO] [te3-small_to_me5-large] 15/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9270
21:36:19 [INFO] [te3-small_to_me5-large] saved → te3-small_to_me5-large.pt  (312.4s)
21:36:19 [INFO]
─── [12/56] te3-small → pplx-embed-1 ───
21:36:19 [INFO] [te3-small_to_pplx-embed-1] 1536d → 1024d  hidden=1536
21:36:40 [INFO] [te3-small_to_pplx-embed-1] 01/15  train_loss=0.00355  test_loss=0.00544  test_cos=0.6627
21:37:00 [INFO] [te3-small_to_pplx-embed-1] 02/15  train_loss=0.00314  test_loss=0.00517  test_cos=0.6813
21:37:21 [INFO] [te3-small_to_pplx-embed-1] 03/15  train_loss=0.00308  test_loss=0.00504  test_cos=0.6902
21:37:42 [INFO] [te3-small_to_pplx-embed-1] 04/15  train_loss=0.00305  test_loss=0.00496  test_cos=0.6961
21:38:03 [INFO] [te3-small_to_pplx-embed-1] 05/15  train_loss=0.00303  test_loss=0.00489  test_cos=0.6998
21:38:24 [INFO] [te3-small_to_pplx-embed-1] 06/15  train_loss=0.00301  test_loss=0.00485  test_cos=0.7023
21:38:45 [INFO] [te3-small_to_pplx-embed-1] 07/15  train_loss=0.00299  test_loss=0.00480  test_cos=0.7046
21:39:05 [INFO] [te3-small_to_pplx-embed-1] 08/15  train_loss=0.00298  test_loss=0.00476  test_cos=0.7068
21:39:26 [INFO] [te3-small_to_pplx-embed-1] 09/15  train_loss=0.00297  test_loss=0.00473  test_cos=0.7086
21:39:47 [INFO] [te3-small_to_pplx-embed-1] 10/15  train_loss=0.00295  test_loss=0.00470  test_cos=0.7104
21:40:07 [INFO] [te3-small_to_pplx-embed-1] 11/15  train_loss=0.00294  test_loss=0.00467  test_cos=0.7120
21:40:28 [INFO] [te3-small_to_pplx-embed-1] 12/15  train_loss=0.00293  test_loss=0.00464  test_cos=0.7136
21:40:48 [INFO] [te3-small_to_pplx-embed-1] 13/15  train_loss=0.00292  test_loss=0.00462  test_cos=0.7152
21:41:09 [INFO] [te3-small_to_pplx-embed-1] 14/15  train_loss=0.00291  test_loss=0.00460  test_cos=0.7164
21:41:29 [INFO] [te3-small_to_pplx-embed-1] 15/15  train_loss=0.00291  test_loss=0.00458  test_cos=0.7177
21:41:29 [INFO] [te3-small_to_pplx-embed-1] saved → te3-small_to_pplx-embed-1.pt  (310.3s)
21:41:29 [INFO]
─── [13/56] te3-small → nemotron-1b-free ───
21:41:29 [INFO] [te3-small_to_nemotron-1b-free] 1536d → 2048d  hidden=2048
21:42:08 [INFO] [te3-small_to_nemotron-1b-free] 01/15  train_loss=0.00011  test_loss=0.00015  test_cos=0.6161
21:42:47 [INFO] [te3-small_to_nemotron-1b-free] 02/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.6269
21:43:26 [INFO] [te3-small_to_nemotron-1b-free] 03/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6383
21:44:05 [INFO] [te3-small_to_nemotron-1b-free] 04/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6472
21:44:44 [INFO] [te3-small_to_nemotron-1b-free] 05/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6520
21:45:23 [INFO] [te3-small_to_nemotron-1b-free] 06/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6545
21:46:02 [INFO] [te3-small_to_nemotron-1b-free] 07/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6575
21:46:41 [INFO] [te3-small_to_nemotron-1b-free] 08/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6595
21:47:22 [INFO] [te3-small_to_nemotron-1b-free] 09/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6605
21:48:05 [INFO] [te3-small_to_nemotron-1b-free] 10/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6618
21:48:49 [INFO] [te3-small_to_nemotron-1b-free] 11/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6632
21:49:32 [INFO] [te3-small_to_nemotron-1b-free] 12/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6637
21:50:13 [INFO] [te3-small_to_nemotron-1b-free] 13/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6647
21:50:52 [INFO] [te3-small_to_nemotron-1b-free] 14/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6655
21:51:29 [INFO] [te3-small_to_nemotron-1b-free] 15/15  train_loss=0.00010  test_loss=0.00014  test_cos=0.6660
21:51:29 [INFO] [te3-small_to_nemotron-1b-free] saved → te3-small_to_nemotron-1b-free.pt  (599.7s)
21:51:29 [INFO]
─── [14/56] te3-small → fastembed-bge-small ───
21:51:29 [INFO] [te3-small_to_fastembed-bge-small] 1536d → 384d  hidden=1536
21:51:45 [INFO] [te3-small_to_fastembed-bge-small] 01/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8473
21:52:00 [INFO] [te3-small_to_fastembed-bge-small] 02/15  train_loss=0.00018  test_loss=0.00036  test_cos=0.8528
21:52:15 [INFO] [te3-small_to_fastembed-bge-small] 03/15  train_loss=0.00018  test_loss=0.00034  test_cos=0.8587
21:52:30 [INFO] [te3-small_to_fastembed-bge-small] 04/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8626
21:52:45 [INFO] [te3-small_to_fastembed-bge-small] 05/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8655
21:53:00 [INFO] [te3-small_to_fastembed-bge-small] 06/15  train_loss=0.00018  test_loss=0.00032  test_cos=0.8673
21:53:15 [INFO] [te3-small_to_fastembed-bge-small] 07/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8678
21:53:30 [INFO] [te3-small_to_fastembed-bge-small] 08/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8685
21:53:45 [INFO] [te3-small_to_fastembed-bge-small] 09/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8691
21:54:00 [INFO] [te3-small_to_fastembed-bge-small] 10/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8701
21:54:15 [INFO] [te3-small_to_fastembed-bge-small] 11/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8708
21:54:29 [INFO] [te3-small_to_fastembed-bge-small] 12/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8702
21:54:44 [INFO] [te3-small_to_fastembed-bge-small] 13/15  train_loss=0.00017  test_loss=0.00031  test_cos=0.8721
21:54:59 [INFO] [te3-small_to_fastembed-bge-small] 14/15  train_loss=0.00017  test_loss=0.00031  test_cos=0.8716
21:55:14 [INFO] [te3-small_to_fastembed-bge-small] 15/15  train_loss=0.00017  test_loss=0.00031  test_cos=0.8725
21:55:14 [INFO] [te3-small_to_fastembed-bge-small] saved → te3-small_to_fastembed-bge-small.pt  (225.4s)
21:55:14 [INFO]
─── [15/56] qwen3-emb-8b → ada-002 ───
21:55:14 [INFO] [qwen3-emb-8b_to_ada-002] 4096d → 1536d  hidden=2048
21:56:12 [INFO] [qwen3-emb-8b_to_ada-002] 01/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9285
21:57:11 [INFO] [qwen3-emb-8b_to_ada-002] 02/15  train_loss=0.00002  test_loss=0.00004  test_cos=0.9355
21:58:10 [INFO] [qwen3-emb-8b_to_ada-002] 03/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9350
21:59:11 [INFO] [qwen3-emb-8b_to_ada-002] 04/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9345
22:00:11 [INFO] [qwen3-emb-8b_to_ada-002] 05/15  train_loss=0.00004  test_loss=0.00004  test_cos=0.9334
22:01:10 [INFO] [qwen3-emb-8b_to_ada-002] 06/15  train_loss=0.00006  test_loss=0.00004  test_cos=0.9333
22:02:12 [INFO] [qwen3-emb-8b_to_ada-002] 07/15  train_loss=0.00007  test_loss=0.00005  test_cos=0.9218
22:03:11 [INFO] [qwen3-emb-8b_to_ada-002] 08/15  train_loss=0.00005  test_loss=0.00004  test_cos=0.9349
22:04:12 [INFO] [qwen3-emb-8b_to_ada-002] 09/15  train_loss=0.00009  test_loss=0.00006  test_cos=0.9073
22:05:12 [INFO] [qwen3-emb-8b_to_ada-002] 10/15  train_loss=0.00004  test_loss=0.00005  test_cos=0.9227
22:06:12 [INFO] [qwen3-emb-8b_to_ada-002] 11/15  train_loss=0.00009  test_loss=0.00005  test_cos=0.9156
22:07:14 [INFO] [qwen3-emb-8b_to_ada-002] 12/15  train_loss=0.00007  test_loss=0.00006  test_cos=0.9134
22:08:14 [INFO] [qwen3-emb-8b_to_ada-002] 13/15  train_loss=0.00005  test_loss=0.00004  test_cos=0.9342
22:09:16 [INFO] [qwen3-emb-8b_to_ada-002] 14/15  train_loss=0.00007  test_loss=0.00006  test_cos=0.9067
22:10:19 [INFO] [qwen3-emb-8b_to_ada-002] 15/15  train_loss=0.00007  test_loss=0.00005  test_cos=0.9248
22:10:19 [INFO] [qwen3-emb-8b_to_ada-002] saved → qwen3-emb-8b_to_ada-002.pt  (904.5s)
22:10:19 [INFO]
─── [16/56] qwen3-emb-8b → te3-small ───
22:10:19 [INFO] [qwen3-emb-8b_to_te3-small] 4096d → 1536d  hidden=2048
22:11:18 [INFO] [qwen3-emb-8b_to_te3-small] 01/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7707
22:12:15 [INFO] [qwen3-emb-8b_to_te3-small] 02/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7806
22:13:14 [INFO] [qwen3-emb-8b_to_te3-small] 03/15  train_loss=0.00012  test_loss=0.00012  test_cos=0.7951
22:14:12 [INFO] [qwen3-emb-8b_to_te3-small] 04/15  train_loss=0.00015  test_loss=0.00011  test_cos=0.8089
22:15:10 [INFO] [qwen3-emb-8b_to_te3-small] 05/15  train_loss=0.00013  test_loss=0.00012  test_cos=0.7903
22:16:11 [INFO] [qwen3-emb-8b_to_te3-small] 06/15  train_loss=0.00015  test_loss=0.00012  test_cos=0.8021
22:17:13 [INFO] [qwen3-emb-8b_to_te3-small] 07/15  train_loss=0.00014  test_loss=0.00014  test_cos=0.7694
22:18:17 [INFO] [qwen3-emb-8b_to_te3-small] 08/15  train_loss=0.00021  test_loss=0.00017  test_cos=0.7355
22:19:19 [INFO] [qwen3-emb-8b_to_te3-small] 09/15  train_loss=0.00013  test_loss=0.00012  test_cos=0.7992
22:20:19 [INFO] [qwen3-emb-8b_to_te3-small] 10/15  train_loss=0.00010  test_loss=0.00011  test_cos=0.8089
22:21:20 [INFO] [qwen3-emb-8b_to_te3-small] 11/15  train_loss=0.00012  test_loss=0.00013  test_cos=0.7854
22:22:20 [INFO] [qwen3-emb-8b_to_te3-small] 12/15  train_loss=0.00011  test_loss=0.00012  test_cos=0.7948
22:23:18 [INFO] [qwen3-emb-8b_to_te3-small] 13/15  train_loss=0.00010  test_loss=0.00012  test_cos=0.7937
22:24:17 [INFO] [qwen3-emb-8b_to_te3-small] 14/15  train_loss=0.00010  test_loss=0.00013  test_cos=0.7892
22:25:15 [INFO] [qwen3-emb-8b_to_te3-small] 15/15  train_loss=0.00009  test_loss=0.00011  test_cos=0.8097
22:25:15 [INFO] [qwen3-emb-8b_to_te3-small] saved → qwen3-emb-8b_to_te3-small.pt  (896.0s)
22:25:15 [INFO]
─── [17/56] qwen3-emb-8b → bge-m3 ───
22:25:15 [INFO] [qwen3-emb-8b_to_bge-m3] 4096d → 1024d  hidden=2048
22:26:08 [INFO] [qwen3-emb-8b_to_bge-m3] 01/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.8131
22:27:01 [INFO] [qwen3-emb-8b_to_bge-m3] 02/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.8257
22:27:54 [INFO] [qwen3-emb-8b_to_bge-m3] 03/15  train_loss=0.00015  test_loss=0.00015  test_cos=0.8290
22:28:47 [INFO] [qwen3-emb-8b_to_bge-m3] 04/15  train_loss=0.00020  test_loss=0.00014  test_cos=0.8420
22:29:40 [INFO] [qwen3-emb-8b_to_bge-m3] 05/15  train_loss=0.00014  test_loss=0.00013  test_cos=0.8530
22:30:32 [INFO] [qwen3-emb-8b_to_bge-m3] 06/15  train_loss=0.00015  test_loss=0.00014  test_cos=0.8447
22:31:25 [INFO] [qwen3-emb-8b_to_bge-m3] 07/15  train_loss=0.00017  test_loss=0.00016  test_cos=0.8229
22:32:18 [INFO] [qwen3-emb-8b_to_bge-m3] 08/15  train_loss=0.00018  test_loss=0.00017  test_cos=0.8123
22:33:10 [INFO] [qwen3-emb-8b_to_bge-m3] 09/15  train_loss=0.00016  test_loss=0.00015  test_cos=0.8348
22:34:03 [INFO] [qwen3-emb-8b_to_bge-m3] 10/15  train_loss=0.00020  test_loss=0.00017  test_cos=0.8208
22:34:54 [INFO] [qwen3-emb-8b_to_bge-m3] 11/15  train_loss=0.00023  test_loss=0.00022  test_cos=0.7736
22:35:44 [INFO] [qwen3-emb-8b_to_bge-m3] 12/15  train_loss=0.00024  test_loss=0.00027  test_cos=0.7413
22:36:35 [INFO] [qwen3-emb-8b_to_bge-m3] 13/15  train_loss=0.00021  test_loss=0.00023  test_cos=0.7736
22:37:27 [INFO] [qwen3-emb-8b_to_bge-m3] 14/15  train_loss=0.00013  test_loss=0.00017  test_cos=0.8129
22:38:20 [INFO] [qwen3-emb-8b_to_bge-m3] 15/15  train_loss=0.00013  test_loss=0.00015  test_cos=0.8319
22:38:20 [INFO] [qwen3-emb-8b_to_bge-m3] saved → qwen3-emb-8b_to_bge-m3.pt  (784.3s)
22:38:20 [INFO]
─── [18/56] qwen3-emb-8b → me5-large ───
22:38:20 [INFO] [qwen3-emb-8b_to_me5-large] 4096d → 1024d  hidden=2048
22:39:13 [INFO] [qwen3-emb-8b_to_me5-large] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9263
22:40:05 [INFO] [qwen3-emb-8b_to_me5-large] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9282
22:40:58 [INFO] [qwen3-emb-8b_to_me5-large] 03/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9280
22:41:50 [INFO] [qwen3-emb-8b_to_me5-large] 04/15  train_loss=0.00008  test_loss=0.00007  test_cos=0.9308
22:42:41 [INFO] [qwen3-emb-8b_to_me5-large] 05/15  train_loss=0.00011  test_loss=0.00007  test_cos=0.9282
22:43:31 [INFO] [qwen3-emb-8b_to_me5-large] 06/15  train_loss=0.00015  test_loss=0.00008  test_cos=0.9210
22:44:21 [INFO] [qwen3-emb-8b_to_me5-large] 07/15  train_loss=0.00008  test_loss=0.00006  test_cos=0.9343
22:45:12 [INFO] [qwen3-emb-8b_to_me5-large] 08/15  train_loss=0.00012  test_loss=0.00007  test_cos=0.9235
22:46:02 [INFO] [qwen3-emb-8b_to_me5-large] 09/15  train_loss=0.00010  test_loss=0.00008  test_cos=0.9137
22:46:52 [INFO] [qwen3-emb-8b_to_me5-large] 10/15  train_loss=0.00011  test_loss=0.00009  test_cos=0.9095
22:47:42 [INFO] [qwen3-emb-8b_to_me5-large] 11/15  train_loss=0.00014  test_loss=0.00014  test_cos=0.8652
22:48:32 [INFO] [qwen3-emb-8b_to_me5-large] 12/15  train_loss=0.00008  test_loss=0.00009  test_cos=0.9070
22:49:22 [INFO] [qwen3-emb-8b_to_me5-large] 13/15  train_loss=0.00010  test_loss=0.00009  test_cos=0.9107
22:50:12 [INFO] [qwen3-emb-8b_to_me5-large] 14/15  train_loss=0.00006  test_loss=0.00006  test_cos=0.9352
22:51:02 [INFO] [qwen3-emb-8b_to_me5-large] 15/15  train_loss=0.00007  test_loss=0.00008  test_cos=0.9207
22:51:02 [INFO] [qwen3-emb-8b_to_me5-large] saved → qwen3-emb-8b_to_me5-large.pt  (762.1s)
22:51:02 [INFO]
─── [19/56] qwen3-emb-8b → pplx-embed-1 ───
22:51:02 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 4096d → 1024d  hidden=2048
22:51:52 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 01/15  train_loss=0.00312  test_loss=0.00460  test_cos=0.7197
22:52:42 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 02/15  train_loss=0.00260  test_loss=0.00417  test_cos=0.7507
22:53:31 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 03/15  train_loss=0.00252  test_loss=0.00399  test_cos=0.7628
22:54:21 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 04/15  train_loss=0.00248  test_loss=0.00390  test_cos=0.7685
22:55:11 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 05/15  train_loss=0.00245  test_loss=0.00383  test_cos=0.7732
22:56:00 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 06/15  train_loss=0.00243  test_loss=0.00378  test_cos=0.7769
22:56:49 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 07/15  train_loss=0.00241  test_loss=0.00374  test_cos=0.7794
22:57:39 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 08/15  train_loss=0.00240  test_loss=0.00371  test_cos=0.7812
22:58:28 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 09/15  train_loss=0.00239  test_loss=0.00368  test_cos=0.7830
22:59:18 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 10/15  train_loss=0.00238  test_loss=0.00366  test_cos=0.7845
23:00:09 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 11/15  train_loss=0.00237  test_loss=0.00363  test_cos=0.7860
23:01:01 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 12/15  train_loss=0.00236  test_loss=0.00360  test_cos=0.7873
23:01:55 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 13/15  train_loss=0.00236  test_loss=0.00358  test_cos=0.7886
23:02:46 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 14/15  train_loss=0.00235  test_loss=0.00357  test_cos=0.7894
23:03:38 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 15/15  train_loss=0.00234  test_loss=0.00355  test_cos=0.7902
23:03:38 [INFO] [qwen3-emb-8b_to_pplx-embed-1] saved → qwen3-emb-8b_to_pplx-embed-1.pt  (755.8s)
23:03:38 [INFO]
─── [20/56] qwen3-emb-8b → nemotron-1b-free ───
23:03:38 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 4096d → 2048d  hidden=2048
23:04:41 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 01/15  train_loss=0.00009  test_loss=0.00013  test_cos=0.6987
23:05:43 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 02/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7216
23:06:45 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 03/15  train_loss=0.00008  test_loss=0.00011  test_cos=0.7325
23:07:47 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 04/15  train_loss=0.00008  test_loss=0.00011  test_cos=0.7390
23:08:49 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 05/15  train_loss=0.00008  test_loss=0.00011  test_cos=0.7459
23:09:52 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 06/15  train_loss=0.00007  test_loss=0.00011  test_cos=0.7512
23:10:55 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 07/15  train_loss=0.00007  test_loss=0.00011  test_cos=0.7533
23:11:58 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 08/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7557
23:13:01 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 09/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7581
23:14:03 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 10/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7601
23:15:06 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 11/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7611
23:16:08 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 12/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7621
23:17:11 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 13/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7628
23:18:11 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 14/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7638
23:19:11 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 15/15  train_loss=0.00007  test_loss=0.00010  test_cos=0.7644
23:19:11 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] saved → qwen3-emb-8b_to_nemotron-1b-free.pt  (932.8s)
23:19:11 [INFO]
─── [21/56] qwen3-emb-8b → fastembed-bge-small ───
23:19:11 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 4096d → 384d  hidden=2048
23:19:55 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 01/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8637
23:20:38 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 02/15  train_loss=0.00019  test_loss=0.00030  test_cos=0.8759
23:21:22 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 03/15  train_loss=0.00023  test_loss=0.00028  test_cos=0.8844
23:22:06 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 04/15  train_loss=0.00027  test_loss=0.00025  test_cos=0.8997
23:22:49 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 05/15  train_loss=0.00020  test_loss=0.00024  test_cos=0.9015
23:23:33 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 06/15  train_loss=0.00025  test_loss=0.00025  test_cos=0.8973
23:24:17 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 07/15  train_loss=0.00021  test_loss=0.00024  test_cos=0.9038
23:25:01 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 08/15  train_loss=0.00024  test_loss=0.00027  test_cos=0.8926
23:25:44 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 09/15  train_loss=0.00031  test_loss=0.00027  test_cos=0.8892
23:26:28 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 10/15  train_loss=0.00019  test_loss=0.00023  test_cos=0.9054
23:27:12 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 11/15  train_loss=0.00022  test_loss=0.00026  test_cos=0.8933
23:27:56 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 12/15  train_loss=0.00022  test_loss=0.00027  test_cos=0.8919
23:28:40 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 13/15  train_loss=0.00022  test_loss=0.00028  test_cos=0.8877
23:29:23 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 14/15  train_loss=0.00020  test_loss=0.00026  test_cos=0.8934
23:30:07 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 15/15  train_loss=0.00020  test_loss=0.00027  test_cos=0.8901
23:30:07 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] saved → qwen3-emb-8b_to_fastembed-bge-small.pt  (656.5s)
23:30:07 [INFO]
─── [22/56] bge-m3 → ada-002 ───
23:30:07 [INFO] [bge-m3_to_ada-002] 1024d → 1536d  hidden=1536
23:30:28 [INFO] [bge-m3_to_ada-002] 01/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.8972
23:30:48 [INFO] [bge-m3_to_ada-002] 02/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9000
23:31:07 [INFO] [bge-m3_to_ada-002] 03/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9020
23:31:28 [INFO] [bge-m3_to_ada-002] 04/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9028
23:31:48 [INFO] [bge-m3_to_ada-002] 05/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9042
23:32:08 [INFO] [bge-m3_to_ada-002] 06/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9057
23:32:27 [INFO] [bge-m3_to_ada-002] 07/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9067
23:32:47 [INFO] [bge-m3_to_ada-002] 08/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9072
23:33:07 [INFO] [bge-m3_to_ada-002] 09/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9077
23:33:26 [INFO] [bge-m3_to_ada-002] 10/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9080
23:33:46 [INFO] [bge-m3_to_ada-002] 11/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9083
23:34:05 [INFO] [bge-m3_to_ada-002] 12/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9085
23:34:25 [INFO] [bge-m3_to_ada-002] 13/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9088
23:34:44 [INFO] [bge-m3_to_ada-002] 14/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9090
23:35:04 [INFO] [bge-m3_to_ada-002] 15/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9091
23:35:04 [INFO] [bge-m3_to_ada-002] saved → bge-m3_to_ada-002.pt  (296.6s)
23:35:04 [INFO]
─── [23/56] bge-m3 → te3-small ───
23:35:04 [INFO] [bge-m3_to_te3-small] 1024d → 1536d  hidden=1536
23:35:23 [INFO] [bge-m3_to_te3-small] 01/15  train_loss=0.00011  test_loss=0.00019  test_cos=0.6573
23:35:43 [INFO] [bge-m3_to_te3-small] 02/15  train_loss=0.00010  test_loss=0.00018  test_cos=0.6671
23:36:02 [INFO] [bge-m3_to_te3-small] 03/15  train_loss=0.00010  test_loss=0.00018  test_cos=0.6738
23:36:21 [INFO] [bge-m3_to_te3-small] 04/15  train_loss=0.00010  test_loss=0.00018  test_cos=0.6772
23:36:40 [INFO] [bge-m3_to_te3-small] 05/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6801
23:37:00 [INFO] [bge-m3_to_te3-small] 06/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6841
23:37:19 [INFO] [bge-m3_to_te3-small] 07/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6864
23:37:38 [INFO] [bge-m3_to_te3-small] 08/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6884
23:37:57 [INFO] [bge-m3_to_te3-small] 09/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6891
23:38:16 [INFO] [bge-m3_to_te3-small] 10/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6912
23:38:35 [INFO] [bge-m3_to_te3-small] 11/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6922
23:38:55 [INFO] [bge-m3_to_te3-small] 12/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6926
23:39:14 [INFO] [bge-m3_to_te3-small] 13/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6935
23:39:33 [INFO] [bge-m3_to_te3-small] 14/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6939
23:39:52 [INFO] [bge-m3_to_te3-small] 15/15  train_loss=0.00010  test_loss=0.00017  test_cos=0.6944
23:39:52 [INFO] [bge-m3_to_te3-small] saved → bge-m3_to_te3-small.pt  (288.2s)
23:39:52 [INFO]
─── [24/56] bge-m3 → qwen3-emb-8b ───
23:39:52 [INFO] [bge-m3_to_qwen3-emb-8b] 1024d → 4096d  hidden=2048
23:40:43 [INFO] [bge-m3_to_qwen3-emb-8b] 01/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6161
23:41:36 [INFO] [bge-m3_to_qwen3-emb-8b] 02/15  train_loss=0.00004  test_loss=0.00008  test_cos=0.6200
23:42:27 [INFO] [bge-m3_to_qwen3-emb-8b] 03/15  train_loss=0.00004  test_loss=0.00008  test_cos=0.6251
23:43:18 [INFO] [bge-m3_to_qwen3-emb-8b] 04/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6283
23:44:10 [INFO] [bge-m3_to_qwen3-emb-8b] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6320
23:45:01 [INFO] [bge-m3_to_qwen3-emb-8b] 06/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6348
23:45:52 [INFO] [bge-m3_to_qwen3-emb-8b] 07/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6374
23:46:44 [INFO] [bge-m3_to_qwen3-emb-8b] 08/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6399
23:47:36 [INFO] [bge-m3_to_qwen3-emb-8b] 09/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6425
23:48:27 [INFO] [bge-m3_to_qwen3-emb-8b] 10/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6450
23:49:19 [INFO] [bge-m3_to_qwen3-emb-8b] 11/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6476
23:50:12 [INFO] [bge-m3_to_qwen3-emb-8b] 12/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6498
23:51:06 [INFO] [bge-m3_to_qwen3-emb-8b] 13/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6506
23:52:00 [INFO] [bge-m3_to_qwen3-emb-8b] 14/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6522
23:52:51 [INFO] [bge-m3_to_qwen3-emb-8b] 15/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6531
23:52:51 [INFO] [bge-m3_to_qwen3-emb-8b] saved → bge-m3_to_qwen3-emb-8b.pt  (779.3s)
23:52:51 [INFO]
─── [25/56] bge-m3 → me5-large ───
23:52:51 [INFO] [bge-m3_to_me5-large] 1024d → 1024d  hidden=1024
23:53:03 [INFO] [bge-m3_to_me5-large] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9284
23:53:15 [INFO] [bge-m3_to_me5-large] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9302
23:53:26 [INFO] [bge-m3_to_me5-large] 03/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9308
23:53:38 [INFO] [bge-m3_to_me5-large] 04/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9313
23:53:50 [INFO] [bge-m3_to_me5-large] 05/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9326
23:54:01 [INFO] [bge-m3_to_me5-large] 06/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9334
23:54:13 [INFO] [bge-m3_to_me5-large] 07/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9341
23:54:24 [INFO] [bge-m3_to_me5-large] 08/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9346
23:54:36 [INFO] [bge-m3_to_me5-large] 09/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9350
23:54:47 [INFO] [bge-m3_to_me5-large] 10/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9352
23:54:58 [INFO] [bge-m3_to_me5-large] 11/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9354
23:55:10 [INFO] [bge-m3_to_me5-large] 12/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9353
23:55:21 [INFO] [bge-m3_to_me5-large] 13/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9355
23:55:33 [INFO] [bge-m3_to_me5-large] 14/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9355
23:55:44 [INFO] [bge-m3_to_me5-large] 15/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9355
23:55:44 [INFO] [bge-m3_to_me5-large] saved → bge-m3_to_me5-large.pt  (172.8s)
23:55:44 [INFO]
─── [26/56] bge-m3 → pplx-embed-1 ───
23:55:44 [INFO] [bge-m3_to_pplx-embed-1] 1024d → 1024d  hidden=1024
23:55:55 [INFO] [bge-m3_to_pplx-embed-1] 01/15  train_loss=0.00424  test_loss=0.00637  test_cos=0.5822
23:56:07 [INFO] [bge-m3_to_pplx-embed-1] 02/15  train_loss=0.00390  test_loss=0.00612  test_cos=0.5996
23:56:18 [INFO] [bge-m3_to_pplx-embed-1] 03/15  train_loss=0.00384  test_loss=0.00602  test_cos=0.6067
23:56:29 [INFO] [bge-m3_to_pplx-embed-1] 04/15  train_loss=0.00379  test_loss=0.00593  test_cos=0.6135
23:56:40 [INFO] [bge-m3_to_pplx-embed-1] 05/15  train_loss=0.00375  test_loss=0.00585  test_cos=0.6208
23:56:51 [INFO] [bge-m3_to_pplx-embed-1] 06/15  train_loss=0.00371  test_loss=0.00576  test_cos=0.6272
23:57:02 [INFO] [bge-m3_to_pplx-embed-1] 07/15  train_loss=0.00368  test_loss=0.00569  test_cos=0.6328
23:57:13 [INFO] [bge-m3_to_pplx-embed-1] 08/15  train_loss=0.00365  test_loss=0.00563  test_cos=0.6377
23:57:24 [INFO] [bge-m3_to_pplx-embed-1] 09/15  train_loss=0.00362  test_loss=0.00556  test_cos=0.6425
23:57:35 [INFO] [bge-m3_to_pplx-embed-1] 10/15  train_loss=0.00360  test_loss=0.00552  test_cos=0.6461
23:57:46 [INFO] [bge-m3_to_pplx-embed-1] 11/15  train_loss=0.00358  test_loss=0.00548  test_cos=0.6495
23:57:57 [INFO] [bge-m3_to_pplx-embed-1] 12/15  train_loss=0.00356  test_loss=0.00544  test_cos=0.6521
23:58:08 [INFO] [bge-m3_to_pplx-embed-1] 13/15  train_loss=0.00354  test_loss=0.00540  test_cos=0.6550
23:58:19 [INFO] [bge-m3_to_pplx-embed-1] 14/15  train_loss=0.00352  test_loss=0.00537  test_cos=0.6574
23:58:30 [INFO] [bge-m3_to_pplx-embed-1] 15/15  train_loss=0.00350  test_loss=0.00533  test_cos=0.6596
23:58:30 [INFO] [bge-m3_to_pplx-embed-1] saved → bge-m3_to_pplx-embed-1.pt  (165.4s)
23:58:30 [INFO]
─── [27/56] bge-m3 → nemotron-1b-free ───
23:58:30 [INFO] [bge-m3_to_nemotron-1b-free] 1024d → 2048d  hidden=2048
23:59:00 [INFO] [bge-m3_to_nemotron-1b-free] 01/15  train_loss=0.00013  test_loss=0.00019  test_cos=0.4986
23:59:30 [INFO] [bge-m3_to_nemotron-1b-free] 02/15  train_loss=0.00012  test_loss=0.00018  test_cos=0.5103
00:00:01 [INFO] [bge-m3_to_nemotron-1b-free] 03/15  train_loss=0.00012  test_loss=0.00018  test_cos=0.5216
00:00:32 [INFO] [bge-m3_to_nemotron-1b-free] 04/15  train_loss=0.00012  test_loss=0.00018  test_cos=0.5287
00:01:03 [INFO] [bge-m3_to_nemotron-1b-free] 05/15  train_loss=0.00012  test_loss=0.00018  test_cos=0.5317
00:01:34 [INFO] [bge-m3_to_nemotron-1b-free] 06/15  train_loss=0.00012  test_loss=0.00018  test_cos=0.5344
00:02:05 [INFO] [bge-m3_to_nemotron-1b-free] 07/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5364
00:02:36 [INFO] [bge-m3_to_nemotron-1b-free] 08/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5383
00:03:06 [INFO] [bge-m3_to_nemotron-1b-free] 09/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5404
00:03:37 [INFO] [bge-m3_to_nemotron-1b-free] 10/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5424
00:04:07 [INFO] [bge-m3_to_nemotron-1b-free] 11/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5436
00:04:37 [INFO] [bge-m3_to_nemotron-1b-free] 12/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5446
00:05:08 [INFO] [bge-m3_to_nemotron-1b-free] 13/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5449
00:05:38 [INFO] [bge-m3_to_nemotron-1b-free] 14/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5465
00:06:08 [INFO] [bge-m3_to_nemotron-1b-free] 15/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5472
00:06:08 [INFO] [bge-m3_to_nemotron-1b-free] saved → bge-m3_to_nemotron-1b-free.pt  (458.5s)
00:06:08 [INFO]
─── [28/56] bge-m3 → fastembed-bge-small ───
00:06:08 [INFO] [bge-m3_to_fastembed-bge-small] 1024d → 384d  hidden=1024
00:06:17 [INFO] [bge-m3_to_fastembed-bge-small] 01/15  train_loss=0.00023  test_loss=0.00043  test_cos=0.8180
00:06:25 [INFO] [bge-m3_to_fastembed-bge-small] 02/15  train_loss=0.00021  test_loss=0.00041  test_cos=0.8266
00:06:33 [INFO] [bge-m3_to_fastembed-bge-small] 03/15  train_loss=0.00021  test_loss=0.00040  test_cos=0.8327
00:06:42 [INFO] [bge-m3_to_fastembed-bge-small] 04/15  train_loss=0.00021  test_loss=0.00039  test_cos=0.8360
00:06:50 [INFO] [bge-m3_to_fastembed-bge-small] 05/15  train_loss=0.00021  test_loss=0.00038  test_cos=0.8398
00:06:58 [INFO] [bge-m3_to_fastembed-bge-small] 06/15  train_loss=0.00021  test_loss=0.00038  test_cos=0.8419
00:07:06 [INFO] [bge-m3_to_fastembed-bge-small] 07/15  train_loss=0.00021  test_loss=0.00038  test_cos=0.8429
00:07:14 [INFO] [bge-m3_to_fastembed-bge-small] 08/15  train_loss=0.00021  test_loss=0.00038  test_cos=0.8440
00:07:23 [INFO] [bge-m3_to_fastembed-bge-small] 09/15  train_loss=0.00021  test_loss=0.00037  test_cos=0.8448
00:07:31 [INFO] [bge-m3_to_fastembed-bge-small] 10/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8457
00:07:39 [INFO] [bge-m3_to_fastembed-bge-small] 11/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8462
00:07:47 [INFO] [bge-m3_to_fastembed-bge-small] 12/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8469
00:07:55 [INFO] [bge-m3_to_fastembed-bge-small] 13/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8471
00:08:03 [INFO] [bge-m3_to_fastembed-bge-small] 14/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8475
00:08:11 [INFO] [bge-m3_to_fastembed-bge-small] 15/15  train_loss=0.00020  test_loss=0.00037  test_cos=0.8481
00:08:11 [INFO] [bge-m3_to_fastembed-bge-small] saved → bge-m3_to_fastembed-bge-small.pt  (123.1s)
00:08:11 [INFO]
─── [29/56] me5-large → ada-002 ───
00:08:11 [INFO] [me5-large_to_ada-002] 1024d → 1536d  hidden=1536
00:08:31 [INFO] [me5-large_to_ada-002] 01/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9049
00:08:50 [INFO] [me5-large_to_ada-002] 02/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.9093
00:09:10 [INFO] [me5-large_to_ada-002] 03/15  train_loss=0.00003  test_loss=0.00006  test_cos=0.9111
00:09:29 [INFO] [me5-large_to_ada-002] 04/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9124
00:09:49 [INFO] [me5-large_to_ada-002] 05/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9137
00:10:09 [INFO] [me5-large_to_ada-002] 06/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9140
00:10:28 [INFO] [me5-large_to_ada-002] 07/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9153
00:10:48 [INFO] [me5-large_to_ada-002] 08/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9156
00:11:09 [INFO] [me5-large_to_ada-002] 09/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9162
00:11:29 [INFO] [me5-large_to_ada-002] 10/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9161
00:11:49 [INFO] [me5-large_to_ada-002] 11/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9172
00:12:10 [INFO] [me5-large_to_ada-002] 12/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9177
00:12:30 [INFO] [me5-large_to_ada-002] 13/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9177
00:12:50 [INFO] [me5-large_to_ada-002] 14/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9179
00:13:10 [INFO] [me5-large_to_ada-002] 15/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9185
00:13:10 [INFO] [me5-large_to_ada-002] saved → me5-large_to_ada-002.pt  (298.6s)
00:13:10 [INFO]
─── [30/56] me5-large → te3-small ───
00:13:10 [INFO] [me5-large_to_te3-small] 1024d → 1536d  hidden=1536
00:13:30 [INFO] [me5-large_to_te3-small] 01/15  train_loss=0.00011  test_loss=0.00017  test_cos=0.6875
00:13:50 [INFO] [me5-large_to_te3-small] 02/15  train_loss=0.00010  test_loss=0.00016  test_cos=0.7030
00:14:09 [INFO] [me5-large_to_te3-small] 03/15  train_loss=0.00010  test_loss=0.00016  test_cos=0.7155
00:14:28 [INFO] [me5-large_to_te3-small] 04/15  train_loss=0.00010  test_loss=0.00016  test_cos=0.7166
00:14:48 [INFO] [me5-large_to_te3-small] 05/15  train_loss=0.00010  test_loss=0.00016  test_cos=0.7220
00:15:07 [INFO] [me5-large_to_te3-small] 06/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7242
00:15:26 [INFO] [me5-large_to_te3-small] 07/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7257
00:15:45 [INFO] [me5-large_to_te3-small] 08/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7292
00:16:04 [INFO] [me5-large_to_te3-small] 09/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7292
00:16:23 [INFO] [me5-large_to_te3-small] 10/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7304
00:16:42 [INFO] [me5-large_to_te3-small] 11/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7313
00:17:01 [INFO] [me5-large_to_te3-small] 12/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7320
00:17:22 [INFO] [me5-large_to_te3-small] 13/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7306
00:17:43 [INFO] [me5-large_to_te3-small] 14/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7337
00:18:04 [INFO] [me5-large_to_te3-small] 15/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.7331
00:18:04 [INFO] [me5-large_to_te3-small] saved → me5-large_to_te3-small.pt  (293.8s)
00:18:04 [INFO]
─── [31/56] me5-large → qwen3-emb-8b ───
00:18:04 [INFO] [me5-large_to_qwen3-emb-8b] 1024d → 4096d  hidden=2048
00:18:59 [INFO] [me5-large_to_qwen3-emb-8b] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.6556
00:19:53 [INFO] [me5-large_to_qwen3-emb-8b] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6691
00:20:47 [INFO] [me5-large_to_qwen3-emb-8b] 03/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6755
00:21:41 [INFO] [me5-large_to_qwen3-emb-8b] 04/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6760
00:22:35 [INFO] [me5-large_to_qwen3-emb-8b] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6798
00:23:28 [INFO] [me5-large_to_qwen3-emb-8b] 06/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6805
00:24:22 [INFO] [me5-large_to_qwen3-emb-8b] 07/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6819
00:25:15 [INFO] [me5-large_to_qwen3-emb-8b] 08/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.6830
00:26:09 [INFO] [me5-large_to_qwen3-emb-8b] 09/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6849
00:27:02 [INFO] [me5-large_to_qwen3-emb-8b] 10/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6867
00:27:53 [INFO] [me5-large_to_qwen3-emb-8b] 11/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6892
00:28:44 [INFO] [me5-large_to_qwen3-emb-8b] 12/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6908
00:29:35 [INFO] [me5-large_to_qwen3-emb-8b] 13/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6921
00:30:27 [INFO] [me5-large_to_qwen3-emb-8b] 14/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6927
00:31:18 [INFO] [me5-large_to_qwen3-emb-8b] 15/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.6940
00:31:18 [INFO] [me5-large_to_qwen3-emb-8b] saved → me5-large_to_qwen3-emb-8b.pt  (794.6s)
00:31:18 [INFO]
─── [32/56] me5-large → bge-m3 ───
00:31:18 [INFO] [me5-large_to_bge-m3] 1024d → 1024d  hidden=1024
00:31:30 [INFO] [me5-large_to_bge-m3] 01/15  train_loss=0.00011  test_loss=0.00013  test_cos=0.8571
00:31:43 [INFO] [me5-large_to_bge-m3] 02/15  train_loss=0.00009  test_loss=0.00013  test_cos=0.8611
00:31:54 [INFO] [me5-large_to_bge-m3] 03/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8656
00:32:06 [INFO] [me5-large_to_bge-m3] 04/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8671
00:32:17 [INFO] [me5-large_to_bge-m3] 05/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8688
00:32:29 [INFO] [me5-large_to_bge-m3] 06/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8703
00:32:40 [INFO] [me5-large_to_bge-m3] 07/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8702
00:32:51 [INFO] [me5-large_to_bge-m3] 08/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8709
00:33:03 [INFO] [me5-large_to_bge-m3] 09/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8717
00:33:14 [INFO] [me5-large_to_bge-m3] 10/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8712
00:33:26 [INFO] [me5-large_to_bge-m3] 11/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8718
00:33:37 [INFO] [me5-large_to_bge-m3] 12/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8720
00:33:49 [INFO] [me5-large_to_bge-m3] 13/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8719
00:34:00 [INFO] [me5-large_to_bge-m3] 14/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8724
00:34:11 [INFO] [me5-large_to_bge-m3] 15/15  train_loss=0.00009  test_loss=0.00012  test_cos=0.8726
00:34:11 [INFO] [me5-large_to_bge-m3] saved → me5-large_to_bge-m3.pt  (172.9s)
00:34:11 [INFO]
─── [33/56] me5-large → pplx-embed-1 ───
00:34:11 [INFO] [me5-large_to_pplx-embed-1] 1024d → 1024d  hidden=1024
00:34:22 [INFO] [me5-large_to_pplx-embed-1] 01/15  train_loss=0.00440  test_loss=0.00599  test_cos=0.5997
00:34:33 [INFO] [me5-large_to_pplx-embed-1] 02/15  train_loss=0.00384  test_loss=0.00566  test_cos=0.6256
00:34:44 [INFO] [me5-large_to_pplx-embed-1] 03/15  train_loss=0.00377  test_loss=0.00555  test_cos=0.6344
00:34:55 [INFO] [me5-large_to_pplx-embed-1] 04/15  train_loss=0.00373  test_loss=0.00550  test_cos=0.6384
00:35:06 [INFO] [me5-large_to_pplx-embed-1] 05/15  train_loss=0.00370  test_loss=0.00545  test_cos=0.6424
00:35:17 [INFO] [me5-large_to_pplx-embed-1] 06/15  train_loss=0.00368  test_loss=0.00541  test_cos=0.6452
00:35:28 [INFO] [me5-large_to_pplx-embed-1] 07/15  train_loss=0.00366  test_loss=0.00536  test_cos=0.6493
00:35:39 [INFO] [me5-large_to_pplx-embed-1] 08/15  train_loss=0.00364  test_loss=0.00533  test_cos=0.6521
00:35:50 [INFO] [me5-large_to_pplx-embed-1] 09/15  train_loss=0.00362  test_loss=0.00529  test_cos=0.6550
00:36:01 [INFO] [me5-large_to_pplx-embed-1] 10/15  train_loss=0.00361  test_loss=0.00525  test_cos=0.6590
00:36:12 [INFO] [me5-large_to_pplx-embed-1] 11/15  train_loss=0.00359  test_loss=0.00521  test_cos=0.6620
00:36:23 [INFO] [me5-large_to_pplx-embed-1] 12/15  train_loss=0.00358  test_loss=0.00519  test_cos=0.6641
00:36:33 [INFO] [me5-large_to_pplx-embed-1] 13/15  train_loss=0.00357  test_loss=0.00516  test_cos=0.6658
00:36:44 [INFO] [me5-large_to_pplx-embed-1] 14/15  train_loss=0.00355  test_loss=0.00514  test_cos=0.6678
00:36:55 [INFO] [me5-large_to_pplx-embed-1] 15/15  train_loss=0.00354  test_loss=0.00510  test_cos=0.6700
00:36:55 [INFO] [me5-large_to_pplx-embed-1] saved → me5-large_to_pplx-embed-1.pt  (163.7s)
00:36:55 [INFO]
─── [34/56] me5-large → nemotron-1b-free ───
00:36:55 [INFO] [me5-large_to_nemotron-1b-free] 1024d → 2048d  hidden=2048
00:37:25 [INFO] [me5-large_to_nemotron-1b-free] 01/15  train_loss=0.00013  test_loss=0.00017  test_cos=0.5393
00:37:55 [INFO] [me5-large_to_nemotron-1b-free] 02/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5562
00:38:25 [INFO] [me5-large_to_nemotron-1b-free] 03/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5604
00:38:55 [INFO] [me5-large_to_nemotron-1b-free] 04/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5667
00:39:25 [INFO] [me5-large_to_nemotron-1b-free] 05/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.5700
00:39:54 [INFO] [me5-large_to_nemotron-1b-free] 06/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5708
00:40:25 [INFO] [me5-large_to_nemotron-1b-free] 07/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5744
00:40:55 [INFO] [me5-large_to_nemotron-1b-free] 08/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5762
00:41:25 [INFO] [me5-large_to_nemotron-1b-free] 09/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5787
00:41:55 [INFO] [me5-large_to_nemotron-1b-free] 10/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5802
00:42:25 [INFO] [me5-large_to_nemotron-1b-free] 11/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5822
00:42:54 [INFO] [me5-large_to_nemotron-1b-free] 12/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5845
00:43:24 [INFO] [me5-large_to_nemotron-1b-free] 13/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5856
00:43:54 [INFO] [me5-large_to_nemotron-1b-free] 14/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5863
00:44:24 [INFO] [me5-large_to_nemotron-1b-free] 15/15  train_loss=0.00012  test_loss=0.00016  test_cos=0.5875
00:44:24 [INFO] [me5-large_to_nemotron-1b-free] saved → me5-large_to_nemotron-1b-free.pt  (449.0s)
00:44:24 [INFO]
─── [35/56] me5-large → fastembed-bge-small ───
00:44:24 [INFO] [me5-large_to_fastembed-bge-small] 1024d → 384d  hidden=1024
00:44:32 [INFO] [me5-large_to_fastembed-bge-small] 01/15  train_loss=0.00022  test_loss=0.00037  test_cos=0.8471
00:44:41 [INFO] [me5-large_to_fastembed-bge-small] 02/15  train_loss=0.00020  test_loss=0.00035  test_cos=0.8556
00:44:49 [INFO] [me5-large_to_fastembed-bge-small] 03/15  train_loss=0.00020  test_loss=0.00034  test_cos=0.8585
00:44:57 [INFO] [me5-large_to_fastembed-bge-small] 04/15  train_loss=0.00020  test_loss=0.00033  test_cos=0.8626
00:45:05 [INFO] [me5-large_to_fastembed-bge-small] 05/15  train_loss=0.00019  test_loss=0.00033  test_cos=0.8648
00:45:14 [INFO] [me5-large_to_fastembed-bge-small] 06/15  train_loss=0.00019  test_loss=0.00032  test_cos=0.8677
00:45:22 [INFO] [me5-large_to_fastembed-bge-small] 07/15  train_loss=0.00019  test_loss=0.00032  test_cos=0.8693
00:45:30 [INFO] [me5-large_to_fastembed-bge-small] 08/15  train_loss=0.00019  test_loss=0.00032  test_cos=0.8697
00:45:38 [INFO] [me5-large_to_fastembed-bge-small] 09/15  train_loss=0.00019  test_loss=0.00032  test_cos=0.8696
00:45:46 [INFO] [me5-large_to_fastembed-bge-small] 10/15  train_loss=0.00019  test_loss=0.00032  test_cos=0.8702
00:45:54 [INFO] [me5-large_to_fastembed-bge-small] 11/15  train_loss=0.00019  test_loss=0.00031  test_cos=0.8712
00:46:02 [INFO] [me5-large_to_fastembed-bge-small] 12/15  train_loss=0.00019  test_loss=0.00031  test_cos=0.8717
00:46:10 [INFO] [me5-large_to_fastembed-bge-small] 13/15  train_loss=0.00019  test_loss=0.00031  test_cos=0.8718
00:46:18 [INFO] [me5-large_to_fastembed-bge-small] 14/15  train_loss=0.00019  test_loss=0.00031  test_cos=0.8729
00:46:26 [INFO] [me5-large_to_fastembed-bge-small] 15/15  train_loss=0.00019  test_loss=0.00031  test_cos=0.8723
00:46:26 [INFO] [me5-large_to_fastembed-bge-small] saved → me5-large_to_fastembed-bge-small.pt  (122.2s)
00:46:26 [INFO]
─── [36/56] pplx-embed-1 → ada-002 ───
00:46:26 [INFO] [pplx-embed-1_to_ada-002] 1024d → 1536d  hidden=1536
00:46:45 [INFO] [pplx-embed-1_to_ada-002] 01/15  train_loss=0.00017  test_loss=0.00009  test_cos=0.8584
00:47:04 [INFO] [pplx-embed-1_to_ada-002] 02/15  train_loss=0.00043  test_loss=0.00017  test_cos=0.7553
00:47:23 [INFO] [pplx-embed-1_to_ada-002] 03/15  train_loss=0.00017  test_loss=0.00009  test_cos=0.8559
00:47:41 [INFO] [pplx-embed-1_to_ada-002] 04/15  train_loss=0.00043  test_loss=0.00019  test_cos=0.7596
00:48:00 [INFO] [pplx-embed-1_to_ada-002] 05/15  train_loss=0.00031  test_loss=0.00017  test_cos=0.7645
00:48:19 [INFO] [pplx-embed-1_to_ada-002] 06/15  train_loss=0.00023  test_loss=0.00017  test_cos=0.7778
00:48:37 [INFO] [pplx-embed-1_to_ada-002] 07/15  train_loss=0.00033  test_loss=0.00027  test_cos=0.7034
00:48:56 [INFO] [pplx-embed-1_to_ada-002] 08/15  train_loss=0.00031  test_loss=0.00028  test_cos=0.6922
00:49:15 [INFO] [pplx-embed-1_to_ada-002] 09/15  train_loss=0.00013  test_loss=0.00018  test_cos=0.7708
00:49:34 [INFO] [pplx-embed-1_to_ada-002] 10/15  train_loss=0.00014  test_loss=0.00025  test_cos=0.7255
00:49:52 [INFO] [pplx-embed-1_to_ada-002] 11/15  train_loss=0.00038  test_loss=0.00040  test_cos=0.6377
00:50:11 [INFO] [pplx-embed-1_to_ada-002] 12/15  train_loss=0.00024  test_loss=0.00035  test_cos=0.6652
00:50:30 [INFO] [pplx-embed-1_to_ada-002] 13/15  train_loss=0.00025  test_loss=0.00065  test_cos=0.6169
00:50:49 [INFO] [pplx-embed-1_to_ada-002] 14/15  train_loss=0.00038  test_loss=0.00101  test_cos=0.5185
00:51:07 [INFO] [pplx-embed-1_to_ada-002] 15/15  train_loss=0.00049  test_loss=0.00103  test_cos=0.5577
00:51:07 [INFO] [pplx-embed-1_to_ada-002] saved → pplx-embed-1_to_ada-002.pt  (281.1s)
00:51:07 [INFO]
─── [37/56] pplx-embed-1 → te3-small ───
00:51:07 [INFO] [pplx-embed-1_to_te3-small] 1024d → 1536d  hidden=1536
00:51:26 [INFO] [pplx-embed-1_to_te3-small] 01/15  train_loss=0.00026  test_loss=0.00022  test_cos=0.5913
00:51:45 [INFO] [pplx-embed-1_to_te3-small] 02/15  train_loss=0.00038  test_loss=0.00022  test_cos=0.6029
00:52:04 [INFO] [pplx-embed-1_to_te3-small] 03/15  train_loss=0.00031  test_loss=0.00020  test_cos=0.6436
00:52:23 [INFO] [pplx-embed-1_to_te3-small] 04/15  train_loss=0.00047  test_loss=0.00025  test_cos=0.5612
00:52:42 [INFO] [pplx-embed-1_to_te3-small] 05/15  train_loss=0.00038  test_loss=0.00028  test_cos=0.5140
00:53:01 [INFO] [pplx-embed-1_to_te3-small] 06/15  train_loss=0.00026  test_loss=0.00025  test_cos=0.5765
00:53:20 [INFO] [pplx-embed-1_to_te3-small] 07/15  train_loss=0.00041  test_loss=0.00036  test_cos=0.4904
00:53:38 [INFO] [pplx-embed-1_to_te3-small] 08/15  train_loss=0.00104  test_loss=0.00080  test_cos=0.3439
00:53:57 [INFO] [pplx-embed-1_to_te3-small] 09/15  train_loss=0.00029  test_loss=0.00043  test_cos=0.4213
00:54:16 [INFO] [pplx-embed-1_to_te3-small] 10/15  train_loss=0.00018  test_loss=0.00028  test_cos=0.5514
00:54:35 [INFO] [pplx-embed-1_to_te3-small] 11/15  train_loss=0.00019  test_loss=0.00028  test_cos=0.5623
00:54:54 [INFO] [pplx-embed-1_to_te3-small] 12/15  train_loss=0.00042  test_loss=0.00045  test_cos=0.4073
00:55:12 [INFO] [pplx-embed-1_to_te3-small] 13/15  train_loss=0.00046  test_loss=0.00052  test_cos=0.4305
00:55:31 [INFO] [pplx-embed-1_to_te3-small] 14/15  train_loss=0.00029  test_loss=0.00046  test_cos=0.3723
00:55:50 [INFO] [pplx-embed-1_to_te3-small] 15/15  train_loss=0.00020  test_loss=0.00042  test_cos=0.4567
00:55:50 [INFO] [pplx-embed-1_to_te3-small] saved → pplx-embed-1_to_te3-small.pt  (282.8s)
00:55:50 [INFO]
─── [38/56] pplx-embed-1 → qwen3-emb-8b ───
00:55:50 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 1024d → 4096d  hidden=2048
00:56:41 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 01/15  train_loss=0.00037  test_loss=0.00016  test_cos=0.3777
00:57:31 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 02/15  train_loss=0.00040  test_loss=0.00017  test_cos=0.4132
00:58:22 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 03/15  train_loss=0.00043  test_loss=0.00029  test_cos=0.3768
00:59:12 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 04/15  train_loss=0.00067  test_loss=0.00044  test_cos=0.2613
01:00:03 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 05/15  train_loss=0.00032  test_loss=0.00038  test_cos=0.2964
01:00:53 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 06/15  train_loss=0.00025  test_loss=0.00038  test_cos=0.3442
01:01:47 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 07/15  train_loss=0.00068  test_loss=0.00131  test_cos=0.2050
01:02:40 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 08/15  train_loss=0.00094  test_loss=0.00134  test_cos=0.1908
01:03:32 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 09/15  train_loss=0.00039  test_loss=0.00045  test_cos=0.2867
01:04:26 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 10/15  train_loss=0.00017  test_loss=0.00025  test_cos=0.3525
01:05:25 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 11/15  train_loss=0.00019  test_loss=0.00037  test_cos=0.3220
01:06:22 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 12/15  train_loss=0.00039  test_loss=0.00053  test_cos=0.2761
01:07:14 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 13/15  train_loss=0.00089  test_loss=0.00158  test_cos=0.2116
01:08:06 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 14/15  train_loss=0.00092  test_loss=0.00154  test_cos=0.1933
01:08:58 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 15/15  train_loss=0.00105  test_loss=0.00187  test_cos=0.1965
01:08:58 [INFO] [pplx-embed-1_to_qwen3-emb-8b] saved → pplx-embed-1_to_qwen3-emb-8b.pt  (787.8s)
01:08:58 [INFO]
─── [39/56] pplx-embed-1 → bge-m3 ───
01:08:58 [INFO] [pplx-embed-1_to_bge-m3] 1024d → 1024d  hidden=1024
01:09:09 [INFO] [pplx-embed-1_to_bge-m3] 01/15  train_loss=0.00018  test_loss=0.00023  test_cos=0.7287
01:09:21 [INFO] [pplx-embed-1_to_bge-m3] 02/15  train_loss=0.00023  test_loss=0.00022  test_cos=0.7467
01:09:32 [INFO] [pplx-embed-1_to_bge-m3] 03/15  train_loss=0.00020  test_loss=0.00020  test_cos=0.7666
01:09:43 [INFO] [pplx-embed-1_to_bge-m3] 04/15  train_loss=0.00023  test_loss=0.00022  test_cos=0.7414
01:09:54 [INFO] [pplx-embed-1_to_bge-m3] 05/15  train_loss=0.00029  test_loss=0.00027  test_cos=0.7036
01:10:05 [INFO] [pplx-embed-1_to_bge-m3] 06/15  train_loss=0.00027  test_loss=0.00027  test_cos=0.6907
01:10:16 [INFO] [pplx-embed-1_to_bge-m3] 07/15  train_loss=0.00022  test_loss=0.00024  test_cos=0.7362
01:10:27 [INFO] [pplx-embed-1_to_bge-m3] 08/15  train_loss=0.00026  test_loss=0.00028  test_cos=0.6970
01:10:38 [INFO] [pplx-embed-1_to_bge-m3] 09/15  train_loss=0.00032  test_loss=0.00032  test_cos=0.6763
01:10:49 [INFO] [pplx-embed-1_to_bge-m3] 10/15  train_loss=0.00023  test_loss=0.00027  test_cos=0.7053
01:11:00 [INFO] [pplx-embed-1_to_bge-m3] 11/15  train_loss=0.00020  test_loss=0.00029  test_cos=0.6818
01:11:11 [INFO] [pplx-embed-1_to_bge-m3] 12/15  train_loss=0.00020  test_loss=0.00031  test_cos=0.6871
01:11:22 [INFO] [pplx-embed-1_to_bge-m3] 13/15  train_loss=0.00027  test_loss=0.00036  test_cos=0.6240
01:11:33 [INFO] [pplx-embed-1_to_bge-m3] 14/15  train_loss=0.00019  test_loss=0.00026  test_cos=0.7167
01:11:44 [INFO] [pplx-embed-1_to_bge-m3] 15/15  train_loss=0.00025  test_loss=0.00039  test_cos=0.6352
01:11:44 [INFO] [pplx-embed-1_to_bge-m3] saved → pplx-embed-1_to_bge-m3.pt  (166.0s)
01:11:44 [INFO]
─── [40/56] pplx-embed-1 → me5-large ───
01:11:44 [INFO] [pplx-embed-1_to_me5-large] 1024d → 1024d  hidden=1024
01:11:55 [INFO] [pplx-embed-1_to_me5-large] 01/15  train_loss=0.00010  test_loss=0.00010  test_cos=0.8882
01:12:06 [INFO] [pplx-embed-1_to_me5-large] 02/15  train_loss=0.00013  test_loss=0.00010  test_cos=0.8953
01:12:17 [INFO] [pplx-embed-1_to_me5-large] 03/15  train_loss=0.00015  test_loss=0.00011  test_cos=0.8805
01:12:28 [INFO] [pplx-embed-1_to_me5-large] 04/15  train_loss=0.00025  test_loss=0.00015  test_cos=0.8495
01:12:39 [INFO] [pplx-embed-1_to_me5-large] 05/15  train_loss=0.00016  test_loss=0.00012  test_cos=0.8721
01:12:50 [INFO] [pplx-embed-1_to_me5-large] 06/15  train_loss=0.00012  test_loss=0.00012  test_cos=0.8709
01:13:01 [INFO] [pplx-embed-1_to_me5-large] 07/15  train_loss=0.00026  test_loss=0.00028  test_cos=0.7589
01:13:12 [INFO] [pplx-embed-1_to_me5-large] 08/15  train_loss=0.00017  test_loss=0.00023  test_cos=0.7982
01:13:23 [INFO] [pplx-embed-1_to_me5-large] 09/15  train_loss=0.00011  test_loss=0.00024  test_cos=0.8037
01:13:34 [INFO] [pplx-embed-1_to_me5-large] 10/15  train_loss=0.00016  test_loss=0.00037  test_cos=0.7492
01:13:45 [INFO] [pplx-embed-1_to_me5-large] 11/15  train_loss=0.00033  test_loss=0.00068  test_cos=0.6550
01:13:56 [INFO] [pplx-embed-1_to_me5-large] 12/15  train_loss=0.00016  test_loss=0.00032  test_cos=0.7585
01:14:07 [INFO] [pplx-embed-1_to_me5-large] 13/15  train_loss=0.00009  test_loss=0.00015  test_cos=0.8461
01:14:18 [INFO] [pplx-embed-1_to_me5-large] 14/15  train_loss=0.00008  test_loss=0.00014  test_cos=0.8563
01:14:29 [INFO] [pplx-embed-1_to_me5-large] 15/15  train_loss=0.00018  test_loss=0.00032  test_cos=0.7496
01:14:29 [INFO] [pplx-embed-1_to_me5-large] saved → pplx-embed-1_to_me5-large.pt  (165.1s)
01:14:29 [INFO]
─── [41/56] pplx-embed-1 → nemotron-1b-free ───
01:14:29 [INFO] [pplx-embed-1_to_nemotron-1b-free] 1024d → 2048d  hidden=2048
01:15:00 [INFO] [pplx-embed-1_to_nemotron-1b-free] 01/15  train_loss=0.00025  test_loss=0.00024  test_cos=0.3658
01:15:31 [INFO] [pplx-embed-1_to_nemotron-1b-free] 02/15  train_loss=0.00083  test_loss=0.00050  test_cos=0.2375
01:16:02 [INFO] [pplx-embed-1_to_nemotron-1b-free] 03/15  train_loss=0.00043  test_loss=0.00032  test_cos=0.3786
01:16:33 [INFO] [pplx-embed-1_to_nemotron-1b-free] 04/15  train_loss=0.00046  test_loss=0.00038  test_cos=0.3377
01:17:04 [INFO] [pplx-embed-1_to_nemotron-1b-free] 05/15  train_loss=0.00066  test_loss=0.00075  test_cos=0.2272
01:17:35 [INFO] [pplx-embed-1_to_nemotron-1b-free] 06/15  train_loss=0.00048  test_loss=0.00063  test_cos=0.2389
01:18:06 [INFO] [pplx-embed-1_to_nemotron-1b-free] 07/15  train_loss=0.00030  test_loss=0.00054  test_cos=0.3129
01:18:37 [INFO] [pplx-embed-1_to_nemotron-1b-free] 08/15  train_loss=0.00059  test_loss=0.00101  test_cos=0.2153
01:19:08 [INFO] [pplx-embed-1_to_nemotron-1b-free] 09/15  train_loss=0.00093  test_loss=0.00121  test_cos=0.1759
01:19:39 [INFO] [pplx-embed-1_to_nemotron-1b-free] 10/15  train_loss=0.00028  test_loss=0.00042  test_cos=0.2946
01:20:10 [INFO] [pplx-embed-1_to_nemotron-1b-free] 11/15  train_loss=0.00025  test_loss=0.00036  test_cos=0.3364
01:20:41 [INFO] [pplx-embed-1_to_nemotron-1b-free] 12/15  train_loss=0.00037  test_loss=0.00057  test_cos=0.2423
01:21:12 [INFO] [pplx-embed-1_to_nemotron-1b-free] 13/15  train_loss=0.00082  test_loss=0.00102  test_cos=0.1776
01:21:43 [INFO] [pplx-embed-1_to_nemotron-1b-free] 14/15  train_loss=0.00092  test_loss=0.00147  test_cos=0.1264
01:22:14 [INFO] [pplx-embed-1_to_nemotron-1b-free] 15/15  train_loss=0.00104  test_loss=0.00155  test_cos=0.1385
01:22:14 [INFO] [pplx-embed-1_to_nemotron-1b-free] saved → pplx-embed-1_to_nemotron-1b-free.pt  (465.0s)
01:22:14 [INFO]
─── [42/56] pplx-embed-1 → fastembed-bge-small ───
01:22:14 [INFO] [pplx-embed-1_to_fastembed-bge-small] 1024d → 384d  hidden=1024
01:22:23 [INFO] [pplx-embed-1_to_fastembed-bge-small] 01/15  train_loss=0.00034  test_loss=0.00050  test_cos=0.7864
01:22:31 [INFO] [pplx-embed-1_to_fastembed-bge-small] 02/15  train_loss=0.00030  test_loss=0.00041  test_cos=0.8262
01:22:39 [INFO] [pplx-embed-1_to_fastembed-bge-small] 03/15  train_loss=0.00030  test_loss=0.00042  test_cos=0.8216
01:22:47 [INFO] [pplx-embed-1_to_fastembed-bge-small] 04/15  train_loss=0.00028  test_loss=0.00042  test_cos=0.8236
01:22:56 [INFO] [pplx-embed-1_to_fastembed-bge-small] 05/15  train_loss=0.00026  test_loss=0.00044  test_cos=0.8136
01:23:04 [INFO] [pplx-embed-1_to_fastembed-bge-small] 06/15  train_loss=0.00029  test_loss=0.00044  test_cos=0.8154
01:23:12 [INFO] [pplx-embed-1_to_fastembed-bge-small] 07/15  train_loss=0.00032  test_loss=0.00046  test_cos=0.8032
01:23:20 [INFO] [pplx-embed-1_to_fastembed-bge-small] 08/15  train_loss=0.00031  test_loss=0.00043  test_cos=0.8194
01:23:28 [INFO] [pplx-embed-1_to_fastembed-bge-small] 09/15  train_loss=0.00031  test_loss=0.00044  test_cos=0.8134
01:23:36 [INFO] [pplx-embed-1_to_fastembed-bge-small] 10/15  train_loss=0.00036  test_loss=0.00046  test_cos=0.8054
01:23:44 [INFO] [pplx-embed-1_to_fastembed-bge-small] 11/15  train_loss=0.00030  test_loss=0.00042  test_cos=0.8246
01:23:53 [INFO] [pplx-embed-1_to_fastembed-bge-small] 12/15  train_loss=0.00029  test_loss=0.00045  test_cos=0.8120
01:24:01 [INFO] [pplx-embed-1_to_fastembed-bge-small] 13/15  train_loss=0.00031  test_loss=0.00046  test_cos=0.8074
01:24:09 [INFO] [pplx-embed-1_to_fastembed-bge-small] 14/15  train_loss=0.00033  test_loss=0.00048  test_cos=0.8000
01:24:17 [INFO] [pplx-embed-1_to_fastembed-bge-small] 15/15  train_loss=0.00031  test_loss=0.00046  test_cos=0.8062
01:24:17 [INFO] [pplx-embed-1_to_fastembed-bge-small] saved → pplx-embed-1_to_fastembed-bge-small.pt  (123.0s)
01:24:17 [INFO]
─── [43/56] nemotron-1b-free → ada-002 ───
01:24:17 [INFO] [nemotron-1b-free_to_ada-002] 2048d → 1536d  hidden=2048
01:24:52 [INFO] [nemotron-1b-free_to_ada-002] 01/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9217
01:25:28 [INFO] [nemotron-1b-free_to_ada-002] 02/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9265
01:26:04 [INFO] [nemotron-1b-free_to_ada-002] 03/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.9279
01:26:40 [INFO] [nemotron-1b-free_to_ada-002] 04/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9291
01:27:16 [INFO] [nemotron-1b-free_to_ada-002] 05/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9295
01:27:54 [INFO] [nemotron-1b-free_to_ada-002] 06/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9306
01:28:31 [INFO] [nemotron-1b-free_to_ada-002] 07/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9318
01:29:12 [INFO] [nemotron-1b-free_to_ada-002] 08/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9324
01:29:51 [INFO] [nemotron-1b-free_to_ada-002] 09/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9327
01:30:28 [INFO] [nemotron-1b-free_to_ada-002] 10/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9334
01:31:05 [INFO] [nemotron-1b-free_to_ada-002] 11/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9338
01:31:43 [INFO] [nemotron-1b-free_to_ada-002] 12/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9341
01:32:21 [INFO] [nemotron-1b-free_to_ada-002] 13/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9343
01:32:59 [INFO] [nemotron-1b-free_to_ada-002] 14/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9345
01:33:36 [INFO] [nemotron-1b-free_to_ada-002] 15/15  train_loss=0.00003  test_loss=0.00004  test_cos=0.9348
01:33:36 [INFO] [nemotron-1b-free_to_ada-002] saved → nemotron-1b-free_to_ada-002.pt  (559.2s)
01:33:36 [INFO]
─── [44/56] nemotron-1b-free → te3-small ───
01:33:36 [INFO] [nemotron-1b-free_to_te3-small] 2048d → 1536d  hidden=2048
01:34:14 [INFO] [nemotron-1b-free_to_te3-small] 01/15  train_loss=0.00009  test_loss=0.00014  test_cos=0.7459
01:34:52 [INFO] [nemotron-1b-free_to_te3-small] 02/15  train_loss=0.00008  test_loss=0.00014  test_cos=0.7580
01:35:29 [INFO] [nemotron-1b-free_to_te3-small] 03/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7664
01:36:08 [INFO] [nemotron-1b-free_to_te3-small] 04/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7753
01:36:52 [INFO] [nemotron-1b-free_to_te3-small] 05/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7801
01:37:32 [INFO] [nemotron-1b-free_to_te3-small] 06/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7837
01:38:08 [INFO] [nemotron-1b-free_to_te3-small] 07/15  train_loss=0.00008  test_loss=0.00013  test_cos=0.7851
01:38:43 [INFO] [nemotron-1b-free_to_te3-small] 08/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7875
01:39:19 [INFO] [nemotron-1b-free_to_te3-small] 09/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7887
01:39:55 [INFO] [nemotron-1b-free_to_te3-small] 10/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7900
01:40:30 [INFO] [nemotron-1b-free_to_te3-small] 11/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7907
01:41:06 [INFO] [nemotron-1b-free_to_te3-small] 12/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7914
01:41:41 [INFO] [nemotron-1b-free_to_te3-small] 13/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7922
01:42:17 [INFO] [nemotron-1b-free_to_te3-small] 14/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7926
01:42:52 [INFO] [nemotron-1b-free_to_te3-small] 15/15  train_loss=0.00008  test_loss=0.00012  test_cos=0.7931
01:42:52 [INFO] [nemotron-1b-free_to_te3-small] saved → nemotron-1b-free_to_te3-small.pt  (555.9s)
01:42:52 [INFO]
─── [45/56] nemotron-1b-free → qwen3-emb-8b ───
01:42:52 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 2048d → 4096d  hidden=2048
01:43:57 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 01/15  train_loss=0.00004  test_loss=0.00006  test_cos=0.7396
01:45:01 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 02/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7539
01:46:05 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 03/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7565
01:47:11 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 04/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7590
01:48:24 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 05/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7604
01:49:32 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 06/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7612
01:50:48 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 07/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7628
01:51:55 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 08/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7653
01:53:03 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 09/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7681
01:54:14 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 10/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7703
01:55:18 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 11/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7720
01:56:22 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 12/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7733
01:57:27 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 13/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7742
01:58:32 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 14/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7751
01:59:37 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 15/15  train_loss=0.00003  test_loss=0.00005  test_cos=0.7761
01:59:37 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] saved → nemotron-1b-free_to_qwen3-emb-8b.pt  (1004.6s)
01:59:37 [INFO]
─── [46/56] nemotron-1b-free → bge-m3 ───
01:59:37 [INFO] [nemotron-1b-free_to_bge-m3] 2048d → 1024d  hidden=2048
02:00:11 [INFO] [nemotron-1b-free_to_bge-m3] 01/15  train_loss=0.00012  test_loss=0.00017  test_cos=0.8077
02:00:45 [INFO] [nemotron-1b-free_to_bge-m3] 02/15  train_loss=0.00011  test_loss=0.00017  test_cos=0.8133
02:01:18 [INFO] [nemotron-1b-free_to_bge-m3] 03/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8192
02:01:52 [INFO] [nemotron-1b-free_to_bge-m3] 04/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8232
02:02:24 [INFO] [nemotron-1b-free_to_bge-m3] 05/15  train_loss=0.00011  test_loss=0.00016  test_cos=0.8249
02:02:55 [INFO] [nemotron-1b-free_to_bge-m3] 06/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8264
02:03:26 [INFO] [nemotron-1b-free_to_bge-m3] 07/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8278
02:03:57 [INFO] [nemotron-1b-free_to_bge-m3] 08/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8289
02:04:29 [INFO] [nemotron-1b-free_to_bge-m3] 09/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8297
02:05:00 [INFO] [nemotron-1b-free_to_bge-m3] 10/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8303
02:05:31 [INFO] [nemotron-1b-free_to_bge-m3] 11/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8309
02:06:02 [INFO] [nemotron-1b-free_to_bge-m3] 12/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8314
02:06:34 [INFO] [nemotron-1b-free_to_bge-m3] 13/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8318
02:07:05 [INFO] [nemotron-1b-free_to_bge-m3] 14/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8323
02:07:36 [INFO] [nemotron-1b-free_to_bge-m3] 15/15  train_loss=0.00010  test_loss=0.00015  test_cos=0.8326
02:07:36 [INFO] [nemotron-1b-free_to_bge-m3] saved → nemotron-1b-free_to_bge-m3.pt  (479.1s)
02:07:36 [INFO]
─── [47/56] nemotron-1b-free → me5-large ───
02:07:36 [INFO] [nemotron-1b-free_to_me5-large] 2048d → 1024d  hidden=2048
02:08:08 [INFO] [nemotron-1b-free_to_me5-large] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.9212
02:08:39 [INFO] [nemotron-1b-free_to_me5-large] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9216
02:09:11 [INFO] [nemotron-1b-free_to_me5-large] 03/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9224
02:09:42 [INFO] [nemotron-1b-free_to_me5-large] 04/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9246
02:10:14 [INFO] [nemotron-1b-free_to_me5-large] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9263
02:10:45 [INFO] [nemotron-1b-free_to_me5-large] 06/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9270
02:11:17 [INFO] [nemotron-1b-free_to_me5-large] 07/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9271
02:11:48 [INFO] [nemotron-1b-free_to_me5-large] 08/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9275
02:12:20 [INFO] [nemotron-1b-free_to_me5-large] 09/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9276
02:12:52 [INFO] [nemotron-1b-free_to_me5-large] 10/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9284
02:13:23 [INFO] [nemotron-1b-free_to_me5-large] 11/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9289
02:13:55 [INFO] [nemotron-1b-free_to_me5-large] 12/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9288
02:14:26 [INFO] [nemotron-1b-free_to_me5-large] 13/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9293
02:14:58 [INFO] [nemotron-1b-free_to_me5-large] 14/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9295
02:15:29 [INFO] [nemotron-1b-free_to_me5-large] 15/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.9297
02:15:29 [INFO] [nemotron-1b-free_to_me5-large] saved → nemotron-1b-free_to_me5-large.pt  (473.0s)
02:15:29 [INFO]
─── [48/56] nemotron-1b-free → pplx-embed-1 ───
02:15:29 [INFO] [nemotron-1b-free_to_pplx-embed-1] 2048d → 1024d  hidden=2048
02:16:01 [INFO] [nemotron-1b-free_to_pplx-embed-1] 01/15  train_loss=0.00349  test_loss=0.00536  test_cos=0.6634
02:16:32 [INFO] [nemotron-1b-free_to_pplx-embed-1] 02/15  train_loss=0.00314  test_loss=0.00510  test_cos=0.6820
02:17:04 [INFO] [nemotron-1b-free_to_pplx-embed-1] 03/15  train_loss=0.00308  test_loss=0.00500  test_cos=0.6890
02:17:39 [INFO] [nemotron-1b-free_to_pplx-embed-1] 04/15  train_loss=0.00304  test_loss=0.00492  test_cos=0.6941
02:18:14 [INFO] [nemotron-1b-free_to_pplx-embed-1] 05/15  train_loss=0.00301  test_loss=0.00485  test_cos=0.6985
02:18:49 [INFO] [nemotron-1b-free_to_pplx-embed-1] 06/15  train_loss=0.00298  test_loss=0.00479  test_cos=0.7026
02:19:25 [INFO] [nemotron-1b-free_to_pplx-embed-1] 07/15  train_loss=0.00296  test_loss=0.00474  test_cos=0.7061
02:20:00 [INFO] [nemotron-1b-free_to_pplx-embed-1] 08/15  train_loss=0.00294  test_loss=0.00469  test_cos=0.7091
02:20:34 [INFO] [nemotron-1b-free_to_pplx-embed-1] 09/15  train_loss=0.00292  test_loss=0.00466  test_cos=0.7118
02:21:08 [INFO] [nemotron-1b-free_to_pplx-embed-1] 10/15  train_loss=0.00290  test_loss=0.00462  test_cos=0.7144
02:21:42 [INFO] [nemotron-1b-free_to_pplx-embed-1] 11/15  train_loss=0.00288  test_loss=0.00459  test_cos=0.7165
02:22:17 [INFO] [nemotron-1b-free_to_pplx-embed-1] 12/15  train_loss=0.00286  test_loss=0.00455  test_cos=0.7187
02:22:52 [INFO] [nemotron-1b-free_to_pplx-embed-1] 13/15  train_loss=0.00285  test_loss=0.00452  test_cos=0.7206
02:23:27 [INFO] [nemotron-1b-free_to_pplx-embed-1] 14/15  train_loss=0.00284  test_loss=0.00450  test_cos=0.7221
02:24:01 [INFO] [nemotron-1b-free_to_pplx-embed-1] 15/15  train_loss=0.00282  test_loss=0.00448  test_cos=0.7237
02:24:01 [INFO] [nemotron-1b-free_to_pplx-embed-1] saved → nemotron-1b-free_to_pplx-embed-1.pt  (511.6s)
02:24:01 [INFO]
─── [49/56] nemotron-1b-free → fastembed-bge-small ───
02:24:01 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 2048d → 384d  hidden=2048
02:24:29 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 01/15  train_loss=0.00020  test_loss=0.00038  test_cos=0.8408
02:24:58 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 02/15  train_loss=0.00019  test_loss=0.00036  test_cos=0.8510
02:25:26 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 03/15  train_loss=0.00018  test_loss=0.00035  test_cos=0.8560
02:25:54 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 04/15  train_loss=0.00018  test_loss=0.00034  test_cos=0.8610
02:26:21 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 05/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8632
02:26:49 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 06/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8644
02:27:16 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 07/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8653
02:27:44 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 08/15  train_loss=0.00018  test_loss=0.00033  test_cos=0.8662
02:28:12 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 09/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8664
02:28:39 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 10/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8670
02:29:05 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 11/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8672
02:29:32 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 12/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8680
02:29:58 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 13/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8683
02:30:24 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 14/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8686
02:30:51 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 15/15  train_loss=0.00017  test_loss=0.00032  test_cos=0.8689
02:30:51 [INFO] [nemotron-1b-free_to_fastembed-bge-small] saved → nemotron-1b-free_to_fastembed-bge-small.pt  (409.5s)
02:30:51 [INFO]
─── [50/56] fastembed-bge-small → ada-002 ───
02:30:51 [INFO] [fastembed-bge-small_to_ada-002] 384d → 1536d  hidden=1536
02:31:08 [INFO] [fastembed-bge-small_to_ada-002] 01/15  train_loss=0.00005  test_loss=0.00007  test_cos=0.8797
02:31:25 [INFO] [fastembed-bge-small_to_ada-002] 02/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8803
02:31:41 [INFO] [fastembed-bge-small_to_ada-002] 03/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8824
02:31:58 [INFO] [fastembed-bge-small_to_ada-002] 04/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8835
02:32:15 [INFO] [fastembed-bge-small_to_ada-002] 05/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8852
02:32:32 [INFO] [fastembed-bge-small_to_ada-002] 06/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8870
02:32:49 [INFO] [fastembed-bge-small_to_ada-002] 07/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8883
02:33:06 [INFO] [fastembed-bge-small_to_ada-002] 08/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8891
02:33:23 [INFO] [fastembed-bge-small_to_ada-002] 09/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8898
02:33:39 [INFO] [fastembed-bge-small_to_ada-002] 10/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8903
02:33:56 [INFO] [fastembed-bge-small_to_ada-002] 11/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8908
02:34:13 [INFO] [fastembed-bge-small_to_ada-002] 12/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8912
02:34:30 [INFO] [fastembed-bge-small_to_ada-002] 13/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8914
02:34:47 [INFO] [fastembed-bge-small_to_ada-002] 14/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8914
02:35:05 [INFO] [fastembed-bge-small_to_ada-002] 15/15  train_loss=0.00004  test_loss=0.00007  test_cos=0.8915
02:35:05 [INFO] [fastembed-bge-small_to_ada-002] saved → fastembed-bge-small_to_ada-002.pt  (254.2s)
02:35:05 [INFO]
─── [51/56] fastembed-bge-small → te3-small ───
02:35:05 [INFO] [fastembed-bge-small_to_te3-small] 384d → 1536d  hidden=1536
02:35:24 [INFO] [fastembed-bge-small_to_te3-small] 01/15  train_loss=0.00012  test_loss=0.00021  test_cos=0.5935
02:35:42 [INFO] [fastembed-bge-small_to_te3-small] 02/15  train_loss=0.00012  test_loss=0.00021  test_cos=0.6006
02:35:59 [INFO] [fastembed-bge-small_to_te3-small] 03/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6104
02:36:16 [INFO] [fastembed-bge-small_to_te3-small] 04/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6148
02:36:33 [INFO] [fastembed-bge-small_to_te3-small] 05/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6170
02:36:50 [INFO] [fastembed-bge-small_to_te3-small] 06/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6208
02:37:06 [INFO] [fastembed-bge-small_to_te3-small] 07/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6240
02:37:23 [INFO] [fastembed-bge-small_to_te3-small] 08/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6260
02:37:39 [INFO] [fastembed-bge-small_to_te3-small] 09/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6259
02:37:56 [INFO] [fastembed-bge-small_to_te3-small] 10/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6273
02:38:13 [INFO] [fastembed-bge-small_to_te3-small] 11/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6260
02:38:29 [INFO] [fastembed-bge-small_to_te3-small] 12/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6269
02:38:46 [INFO] [fastembed-bge-small_to_te3-small] 13/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6255
02:39:03 [INFO] [fastembed-bge-small_to_te3-small] 14/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6265
02:39:19 [INFO] [fastembed-bge-small_to_te3-small] 15/15  train_loss=0.00012  test_loss=0.00020  test_cos=0.6260
02:39:19 [INFO] [fastembed-bge-small_to_te3-small] saved → fastembed-bge-small_to_te3-small.pt  (254.4s)
02:39:19 [INFO]
─── [52/56] fastembed-bge-small → qwen3-emb-8b ───
02:39:19 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 384d → 4096d  hidden=2048
02:40:12 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 01/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5843
02:41:05 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 02/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5884
02:41:58 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 03/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5900
02:42:51 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 04/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5914
02:43:44 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 05/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5936
02:44:37 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 06/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5954
02:45:30 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 07/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5971
02:46:23 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 08/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.5987
02:47:16 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 09/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6001
02:48:09 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 10/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6011
02:49:03 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 11/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6018
02:49:56 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 12/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6019
02:50:49 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 13/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6025
02:51:42 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 14/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6030
02:52:35 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 15/15  train_loss=0.00005  test_loss=0.00008  test_cos=0.6031
02:52:35 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] saved → fastembed-bge-small_to_qwen3-emb-8b.pt  (795.3s)
02:52:35 [INFO]
─── [53/56] fastembed-bge-small → bge-m3 ───
02:52:35 [INFO] [fastembed-bge-small_to_bge-m3] 384d → 1024d  hidden=1024
02:52:45 [INFO] [fastembed-bge-small_to_bge-m3] 01/15  train_loss=0.00015  test_loss=0.00022  test_cos=0.7400
02:52:54 [INFO] [fastembed-bge-small_to_bge-m3] 02/15  train_loss=0.00015  test_loss=0.00022  test_cos=0.7398
02:53:03 [INFO] [fastembed-bge-small_to_bge-m3] 03/15  train_loss=0.00015  test_loss=0.00022  test_cos=0.7446
02:53:13 [INFO] [fastembed-bge-small_to_bge-m3] 04/15  train_loss=0.00015  test_loss=0.00022  test_cos=0.7476
02:53:22 [INFO] [fastembed-bge-small_to_bge-m3] 05/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7499
02:53:31 [INFO] [fastembed-bge-small_to_bge-m3] 06/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7509
02:53:41 [INFO] [fastembed-bge-small_to_bge-m3] 07/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7520
02:53:50 [INFO] [fastembed-bge-small_to_bge-m3] 08/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7535
02:53:59 [INFO] [fastembed-bge-small_to_bge-m3] 09/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7542
02:54:08 [INFO] [fastembed-bge-small_to_bge-m3] 10/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7549
02:54:18 [INFO] [fastembed-bge-small_to_bge-m3] 11/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7554
02:54:27 [INFO] [fastembed-bge-small_to_bge-m3] 12/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7554
02:54:36 [INFO] [fastembed-bge-small_to_bge-m3] 13/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7557
02:54:45 [INFO] [fastembed-bge-small_to_bge-m3] 14/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7558
02:54:54 [INFO] [fastembed-bge-small_to_bge-m3] 15/15  train_loss=0.00015  test_loss=0.00021  test_cos=0.7563
02:54:54 [INFO] [fastembed-bge-small_to_bge-m3] saved → fastembed-bge-small_to_bge-m3.pt  (139.4s)
02:54:54 [INFO]
─── [54/56] fastembed-bge-small → me5-large ───
02:54:54 [INFO] [fastembed-bge-small_to_me5-large] 384d → 1024d  hidden=1024
02:55:04 [INFO] [fastembed-bge-small_to_me5-large] 01/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9001
02:55:13 [INFO] [fastembed-bge-small_to_me5-large] 02/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9005
02:55:22 [INFO] [fastembed-bge-small_to_me5-large] 03/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.8990
02:55:32 [INFO] [fastembed-bge-small_to_me5-large] 04/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.8998
02:55:41 [INFO] [fastembed-bge-small_to_me5-large] 05/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9016
02:55:50 [INFO] [fastembed-bge-small_to_me5-large] 06/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9027
02:55:59 [INFO] [fastembed-bge-small_to_me5-large] 07/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9037
02:56:09 [INFO] [fastembed-bge-small_to_me5-large] 08/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9045
02:56:18 [INFO] [fastembed-bge-small_to_me5-large] 09/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9049
02:56:27 [INFO] [fastembed-bge-small_to_me5-large] 10/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9049
02:56:36 [INFO] [fastembed-bge-small_to_me5-large] 11/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9048
02:56:45 [INFO] [fastembed-bge-small_to_me5-large] 12/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9049
02:56:54 [INFO] [fastembed-bge-small_to_me5-large] 13/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9050
02:57:03 [INFO] [fastembed-bge-small_to_me5-large] 14/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9050
02:57:13 [INFO] [fastembed-bge-small_to_me5-large] 15/15  train_loss=0.00006  test_loss=0.00009  test_cos=0.9052
02:57:13 [INFO] [fastembed-bge-small_to_me5-large] saved → fastembed-bge-small_to_me5-large.pt  (138.5s)
02:57:13 [INFO]
─── [55/56] fastembed-bge-small → pplx-embed-1 ───
02:57:13 [INFO] [fastembed-bge-small_to_pplx-embed-1] 384d → 1024d  hidden=1024
02:57:22 [INFO] [fastembed-bge-small_to_pplx-embed-1] 01/15  train_loss=0.00458  test_loss=0.00658  test_cos=0.5417
02:57:31 [INFO] [fastembed-bge-small_to_pplx-embed-1] 02/15  train_loss=0.00435  test_loss=0.00647  test_cos=0.5504
02:57:41 [INFO] [fastembed-bge-small_to_pplx-embed-1] 03/15  train_loss=0.00433  test_loss=0.00645  test_cos=0.5530
02:57:50 [INFO] [fastembed-bge-small_to_pplx-embed-1] 04/15  train_loss=0.00432  test_loss=0.00643  test_cos=0.5555
02:57:59 [INFO] [fastembed-bge-small_to_pplx-embed-1] 05/15  train_loss=0.00430  test_loss=0.00642  test_cos=0.5566
02:58:08 [INFO] [fastembed-bge-small_to_pplx-embed-1] 06/15  train_loss=0.00428  test_loss=0.00638  test_cos=0.5605
02:58:17 [INFO] [fastembed-bge-small_to_pplx-embed-1] 07/15  train_loss=0.00426  test_loss=0.00634  test_cos=0.5638
02:58:26 [INFO] [fastembed-bge-small_to_pplx-embed-1] 08/15  train_loss=0.00424  test_loss=0.00629  test_cos=0.5677
02:58:36 [INFO] [fastembed-bge-small_to_pplx-embed-1] 09/15  train_loss=0.00422  test_loss=0.00625  test_cos=0.5710
02:58:45 [INFO] [fastembed-bge-small_to_pplx-embed-1] 10/15  train_loss=0.00421  test_loss=0.00622  test_cos=0.5736
02:58:54 [INFO] [fastembed-bge-small_to_pplx-embed-1] 11/15  train_loss=0.00419  test_loss=0.00618  test_cos=0.5771
02:59:03 [INFO] [fastembed-bge-small_to_pplx-embed-1] 12/15  train_loss=0.00417  test_loss=0.00614  test_cos=0.5803
02:59:13 [INFO] [fastembed-bge-small_to_pplx-embed-1] 13/15  train_loss=0.00416  test_loss=0.00612  test_cos=0.5826
02:59:23 [INFO] [fastembed-bge-small_to_pplx-embed-1] 14/15  train_loss=0.00414  test_loss=0.00609  test_cos=0.5857
02:59:32 [INFO] [fastembed-bge-small_to_pplx-embed-1] 15/15  train_loss=0.00413  test_loss=0.00606  test_cos=0.5880
02:59:32 [INFO] [fastembed-bge-small_to_pplx-embed-1] saved → fastembed-bge-small_to_pplx-embed-1.pt  (139.7s)
02:59:32 [INFO]
─── [56/56] fastembed-bge-small → nemotron-1b-free ───
02:59:32 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 384d → 2048d  hidden=2048
03:00:01 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 01/15  train_loss=0.00014  test_loss=0.00021  test_cos=0.4113
03:00:31 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 02/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4152
03:01:01 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 03/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4247
03:01:33 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 04/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4327
03:02:03 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 05/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4386
03:02:32 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 06/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4426
03:03:01 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 07/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4466
03:03:29 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 08/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4483
03:03:58 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 09/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4490
03:04:26 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 10/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4501
03:04:55 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 11/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4511
03:05:23 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 12/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4519
03:05:52 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 13/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4514
03:06:21 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 14/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4537
03:06:49 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 15/15  train_loss=0.00014  test_loss=0.00020  test_cos=0.4534
03:06:49 [INFO] [fastembed-bge-small_to_nemotron-1b-free] saved → fastembed-bge-small_to_nemotron-1b-free.pt  (436.8s)
03:06:49 [INFO]
All done in 413.5 min
Models   → /Users/gigadelux/Documents/PROJECTS/queryn/queryn/AI/models/
Summary  → /Users/gigadelux/Documents/PROJECTS/queryn/queryn/AI/reports/training_summary.json
