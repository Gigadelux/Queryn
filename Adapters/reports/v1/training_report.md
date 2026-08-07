python3 v1_adapter_model_training.py
19:44:52 [INFO] Device: mps  |  Pairs: 49  |  Architectures: ['linear', 'deep']  |  Epochs: 15  |  Batch: 128
19:44:52 [INFO]
─── [1/49] ada-002 → te3-small ───
19:44:52 [INFO] [ada-002_to_te3-small] 1536d → 1536d
19:45:08 [INFO] [ada-002_to_te3-small][linear] 01/15  train_loss=0.12578  test_loss=0.17040  test_cos=0.8296  lr=1.00e-03
19:45:22 [INFO] [ada-002_to_te3-small][linear] 02/15  train_loss=0.10734  test_loss=0.15729  test_cos=0.8427  lr=1.00e-03
19:45:37 [INFO] [ada-002_to_te3-small][linear] 03/15  train_loss=0.10525  test_loss=0.15069  test_cos=0.8493  lr=1.00e-03
19:45:52 [INFO] [ada-002_to_te3-small][linear] 04/15  train_loss=0.10414  test_loss=0.14608  test_cos=0.8539  lr=1.00e-03
19:46:07 [INFO] [ada-002_to_te3-small][linear] 05/15  train_loss=0.10340  test_loss=0.14262  test_cos=0.8574  lr=1.00e-03
19:46:22 [INFO] [ada-002_to_te3-small][linear] 06/15  train_loss=0.10286  test_loss=0.13989  test_cos=0.8601  lr=1.00e-03
19:46:37 [INFO] [ada-002_to_te3-small][linear] 07/15  train_loss=0.10245  test_loss=0.13764  test_cos=0.8624  lr=1.00e-03
19:46:52 [INFO] [ada-002_to_te3-small][linear] 08/15  train_loss=0.10212  test_loss=0.13575  test_cos=0.8643  lr=1.00e-03
19:47:07 [INFO] [ada-002_to_te3-small][linear] 09/15  train_loss=0.10184  test_loss=0.13414  test_cos=0.8659  lr=1.00e-03
19:47:22 [INFO] [ada-002_to_te3-small][linear] 10/15  train_loss=0.10161  test_loss=0.13277  test_cos=0.8672  lr=1.00e-03
19:47:37 [INFO] [ada-002_to_te3-small][linear] 11/15  train_loss=0.10142  test_loss=0.13159  test_cos=0.8684  lr=1.00e-03
19:47:51 [INFO] [ada-002_to_te3-small][linear] 12/15  train_loss=0.10125  test_loss=0.13057  test_cos=0.8694  lr=1.00e-03
19:48:05 [INFO] [ada-002_to_te3-small][linear] 13/15  train_loss=0.10110  test_loss=0.12969  test_cos=0.8703  lr=1.00e-03
19:48:19 [INFO] [ada-002_to_te3-small][linear] 14/15  train_loss=0.10097  test_loss=0.12892  test_cos=0.8711  lr=1.00e-03
19:48:33 [INFO] [ada-002_to_te3-small][linear] 15/15  train_loss=0.10085  test_loss=0.12824  test_cos=0.8718  lr=1.00e-03
19:48:48 [INFO] [ada-002_to_te3-small][deep] 01/15  train_loss=0.14596  test_loss=0.19796  test_cos=0.8020  lr=1.00e-03
19:49:02 [INFO] [ada-002_to_te3-small][deep] 02/15  train_loss=0.11272  test_loss=0.17557  test_cos=0.8244  lr=1.00e-03
19:49:16 [INFO] [ada-002_to_te3-small][deep] 03/15  train_loss=0.10892  test_loss=0.16385  test_cos=0.8362  lr=1.00e-03
19:49:30 [INFO] [ada-002_to_te3-small][deep] 04/15  train_loss=0.10701  test_loss=0.15838  test_cos=0.8416  lr=1.00e-03
19:49:44 [INFO] [ada-002_to_te3-small][deep] 05/15  train_loss=0.10580  test_loss=0.15412  test_cos=0.8459  lr=1.00e-03
19:49:58 [INFO] [ada-002_to_te3-small][deep] 06/15  train_loss=0.10492  test_loss=0.15042  test_cos=0.8496  lr=1.00e-03
19:50:13 [INFO] [ada-002_to_te3-small][deep] 07/15  train_loss=0.10425  test_loss=0.14763  test_cos=0.8524  lr=1.00e-03
19:50:27 [INFO] [ada-002_to_te3-small][deep] 08/15  train_loss=0.10372  test_loss=0.14535  test_cos=0.8546  lr=1.00e-03
19:50:41 [INFO] [ada-002_to_te3-small][deep] 09/15  train_loss=0.10330  test_loss=0.14345  test_cos=0.8566  lr=1.00e-03
19:50:55 [INFO] [ada-002_to_te3-small][deep] 10/15  train_loss=0.10294  test_loss=0.14174  test_cos=0.8583  lr=1.00e-03
19:51:09 [INFO] [ada-002_to_te3-small][deep] 11/15  train_loss=0.10261  test_loss=0.14014  test_cos=0.8599  lr=1.00e-03
19:51:24 [INFO] [ada-002_to_te3-small][deep] 12/15  train_loss=0.10232  test_loss=0.13869  test_cos=0.8613  lr=1.00e-03
19:51:38 [INFO] [ada-002_to_te3-small][deep] 13/15  train_loss=0.10206  test_loss=0.13744  test_cos=0.8626  lr=1.00e-03
19:51:52 [INFO] [ada-002_to_te3-small][deep] 14/15  train_loss=0.10182  test_loss=0.13625  test_cos=0.8637  lr=1.00e-03
19:52:06 [INFO] [ada-002_to_te3-small][deep] 15/15  train_loss=0.10159  test_loss=0.13515  test_cos=0.8648  lr=1.00e-03
19:52:06 [INFO] [ada-002_to_te3-small] winner=linear best_epoch=15 best_test_cos=0.8718 saved → ada-002_to_te3-small.pt  (433.7s)
19:52:06 [INFO]
─── [2/49] ada-002 → qwen3-emb-8b ───
19:52:06 [INFO] [ada-002_to_qwen3-emb-8b] 1536d → 4096d
19:52:45 [INFO] [ada-002_to_qwen3-emb-8b][linear] 01/15  train_loss=0.17371  test_loss=0.26421  test_cos=0.7358  lr=1.00e-03
19:53:24 [INFO] [ada-002_to_qwen3-emb-8b][linear] 02/15  train_loss=0.15435  test_loss=0.24457  test_cos=0.7554  lr=1.00e-03
19:54:01 [INFO] [ada-002_to_qwen3-emb-8b][linear] 03/15  train_loss=0.15149  test_loss=0.23420  test_cos=0.7658  lr=1.00e-03
19:54:38 [INFO] [ada-002_to_qwen3-emb-8b][linear] 04/15  train_loss=0.15001  test_loss=0.22721  test_cos=0.7728  lr=1.00e-03
19:55:14 [INFO] [ada-002_to_qwen3-emb-8b][linear] 05/15  train_loss=0.14904  test_loss=0.22213  test_cos=0.7779  lr=1.00e-03
19:55:53 [INFO] [ada-002_to_qwen3-emb-8b][linear] 06/15  train_loss=0.14835  test_loss=0.21828  test_cos=0.7817  lr=1.00e-03
19:56:33 [INFO] [ada-002_to_qwen3-emb-8b][linear] 07/15  train_loss=0.14781  test_loss=0.21525  test_cos=0.7847  lr=1.00e-03
19:57:13 [INFO] [ada-002_to_qwen3-emb-8b][linear] 08/15  train_loss=0.14739  test_loss=0.21278  test_cos=0.7872  lr=1.00e-03
19:57:55 [INFO] [ada-002_to_qwen3-emb-8b][linear] 09/15  train_loss=0.14704  test_loss=0.21067  test_cos=0.7893  lr=1.00e-03
19:58:32 [INFO] [ada-002_to_qwen3-emb-8b][linear] 10/15  train_loss=0.14674  test_loss=0.20882  test_cos=0.7912  lr=1.00e-03
19:59:09 [INFO] [ada-002_to_qwen3-emb-8b][linear] 11/15  train_loss=0.14649  test_loss=0.20715  test_cos=0.7929  lr=1.00e-03
19:59:45 [INFO] [ada-002_to_qwen3-emb-8b][linear] 12/15  train_loss=0.14627  test_loss=0.20561  test_cos=0.7944  lr=1.00e-03
20:00:22 [INFO] [ada-002_to_qwen3-emb-8b][linear] 13/15  train_loss=0.14608  test_loss=0.20417  test_cos=0.7958  lr=1.00e-03
20:00:59 [INFO] [ada-002_to_qwen3-emb-8b][linear] 14/15  train_loss=0.14591  test_loss=0.20282  test_cos=0.7972  lr=1.00e-03
20:01:36 [INFO] [ada-002_to_qwen3-emb-8b][linear] 15/15  train_loss=0.14576  test_loss=0.20153  test_cos=0.7985  lr=1.00e-03
20:02:05 [INFO] [ada-002_to_qwen3-emb-8b][deep] 01/15  train_loss=0.20002  test_loss=0.29384  test_cos=0.7062  lr=1.00e-03
20:02:34 [INFO] [ada-002_to_qwen3-emb-8b][deep] 02/15  train_loss=0.16038  test_loss=0.25983  test_cos=0.7402  lr=1.00e-03
20:03:04 [INFO] [ada-002_to_qwen3-emb-8b][deep] 03/15  train_loss=0.15520  test_loss=0.25041  test_cos=0.7496  lr=1.00e-03
20:03:34 [INFO] [ada-002_to_qwen3-emb-8b][deep] 04/15  train_loss=0.15251  test_loss=0.24210  test_cos=0.7579  lr=1.00e-03
20:04:04 [INFO] [ada-002_to_qwen3-emb-8b][deep] 05/15  train_loss=0.15082  test_loss=0.23553  test_cos=0.7645  lr=1.00e-03
20:04:34 [INFO] [ada-002_to_qwen3-emb-8b][deep] 06/15  train_loss=0.14961  test_loss=0.23090  test_cos=0.7691  lr=1.00e-03
20:05:05 [INFO] [ada-002_to_qwen3-emb-8b][deep] 07/15  train_loss=0.14866  test_loss=0.22691  test_cos=0.7731  lr=1.00e-03
20:05:35 [INFO] [ada-002_to_qwen3-emb-8b][deep] 08/15  train_loss=0.14787  test_loss=0.22358  test_cos=0.7764  lr=1.00e-03
20:06:05 [INFO] [ada-002_to_qwen3-emb-8b][deep] 09/15  train_loss=0.14720  test_loss=0.22098  test_cos=0.7790  lr=1.00e-03
20:06:36 [INFO] [ada-002_to_qwen3-emb-8b][deep] 10/15  train_loss=0.14660  test_loss=0.21810  test_cos=0.7819  lr=1.00e-03
20:07:07 [INFO] [ada-002_to_qwen3-emb-8b][deep] 11/15  train_loss=0.14606  test_loss=0.21552  test_cos=0.7845  lr=1.00e-03
20:07:38 [INFO] [ada-002_to_qwen3-emb-8b][deep] 12/15  train_loss=0.14557  test_loss=0.21274  test_cos=0.7873  lr=1.00e-03
20:08:09 [INFO] [ada-002_to_qwen3-emb-8b][deep] 13/15  train_loss=0.14510  test_loss=0.21008  test_cos=0.7899  lr=1.00e-03
20:08:39 [INFO] [ada-002_to_qwen3-emb-8b][deep] 14/15  train_loss=0.14466  test_loss=0.20752  test_cos=0.7925  lr=1.00e-03
20:09:10 [INFO] [ada-002_to_qwen3-emb-8b][deep] 15/15  train_loss=0.14424  test_loss=0.20513  test_cos=0.7949  lr=1.00e-03
20:09:10 [INFO] [ada-002_to_qwen3-emb-8b] winner=linear best_epoch=15 best_test_cos=0.7985 saved → ada-002_to_qwen3-emb-8b.pt  (1010.8s)
20:09:10 [INFO]
─── [3/49] ada-002 → bge-m3 ───
20:09:10 [INFO] [ada-002_to_bge-m3] 1536d → 1024d
20:09:22 [INFO] [ada-002_to_bge-m3][linear] 01/15  train_loss=0.13016  test_loss=0.15761  test_cos=0.8424  lr=1.00e-03
20:09:34 [INFO] [ada-002_to_bge-m3][linear] 02/15  train_loss=0.11658  test_loss=0.14911  test_cos=0.8509  lr=1.00e-03
20:09:46 [INFO] [ada-002_to_bge-m3][linear] 03/15  train_loss=0.11479  test_loss=0.14469  test_cos=0.8553  lr=1.00e-03
20:09:58 [INFO] [ada-002_to_bge-m3][linear] 04/15  train_loss=0.11381  test_loss=0.14176  test_cos=0.8582  lr=1.00e-03
20:10:10 [INFO] [ada-002_to_bge-m3][linear] 05/15  train_loss=0.11317  test_loss=0.13972  test_cos=0.8603  lr=1.00e-03
20:10:21 [INFO] [ada-002_to_bge-m3][linear] 06/15  train_loss=0.11269  test_loss=0.13828  test_cos=0.8617  lr=1.00e-03
20:10:33 [INFO] [ada-002_to_bge-m3][linear] 07/15  train_loss=0.11232  test_loss=0.13722  test_cos=0.8628  lr=1.00e-03
20:10:45 [INFO] [ada-002_to_bge-m3][linear] 08/15  train_loss=0.11202  test_loss=0.13642  test_cos=0.8636  lr=1.00e-03
20:10:57 [INFO] [ada-002_to_bge-m3][linear] 09/15  train_loss=0.11177  test_loss=0.13579  test_cos=0.8642  lr=1.00e-03
20:11:09 [INFO] [ada-002_to_bge-m3][linear] 10/15  train_loss=0.11156  test_loss=0.13526  test_cos=0.8647  lr=1.00e-03
20:11:21 [INFO] [ada-002_to_bge-m3][linear] 11/15  train_loss=0.11138  test_loss=0.13479  test_cos=0.8652  lr=1.00e-03
20:11:33 [INFO] [ada-002_to_bge-m3][linear] 12/15  train_loss=0.11123  test_loss=0.13436  test_cos=0.8656  lr=1.00e-03
20:11:45 [INFO] [ada-002_to_bge-m3][linear] 13/15  train_loss=0.11109  test_loss=0.13395  test_cos=0.8660  lr=1.00e-03
20:11:57 [INFO] [ada-002_to_bge-m3][linear] 14/15  train_loss=0.11097  test_loss=0.13356  test_cos=0.8664  lr=1.00e-03
20:12:08 [INFO] [ada-002_to_bge-m3][linear] 15/15  train_loss=0.11085  test_loss=0.13317  test_cos=0.8668  lr=1.00e-03
20:12:19 [INFO] [ada-002_to_bge-m3][deep] 01/15  train_loss=0.14355  test_loss=0.17508  test_cos=0.8249  lr=1.00e-03
20:12:30 [INFO] [ada-002_to_bge-m3][deep] 02/15  train_loss=0.11905  test_loss=0.16074  test_cos=0.8393  lr=1.00e-03
20:12:41 [INFO] [ada-002_to_bge-m3][deep] 03/15  train_loss=0.11638  test_loss=0.15442  test_cos=0.8456  lr=1.00e-03
20:12:52 [INFO] [ada-002_to_bge-m3][deep] 04/15  train_loss=0.11500  test_loss=0.15048  test_cos=0.8495  lr=1.00e-03
20:13:03 [INFO] [ada-002_to_bge-m3][deep] 05/15  train_loss=0.11413  test_loss=0.14792  test_cos=0.8521  lr=1.00e-03
20:13:14 [INFO] [ada-002_to_bge-m3][deep] 06/15  train_loss=0.11350  test_loss=0.14519  test_cos=0.8548  lr=1.00e-03
20:13:25 [INFO] [ada-002_to_bge-m3][deep] 07/15  train_loss=0.11301  test_loss=0.14321  test_cos=0.8568  lr=1.00e-03
20:13:35 [INFO] [ada-002_to_bge-m3][deep] 08/15  train_loss=0.11261  test_loss=0.14165  test_cos=0.8584  lr=1.00e-03
20:13:46 [INFO] [ada-002_to_bge-m3][deep] 09/15  train_loss=0.11229  test_loss=0.14028  test_cos=0.8597  lr=1.00e-03
20:13:57 [INFO] [ada-002_to_bge-m3][deep] 10/15  train_loss=0.11201  test_loss=0.13908  test_cos=0.8609  lr=1.00e-03
20:14:08 [INFO] [ada-002_to_bge-m3][deep] 11/15  train_loss=0.11177  test_loss=0.13808  test_cos=0.8619  lr=1.00e-03
20:14:19 [INFO] [ada-002_to_bge-m3][deep] 12/15  train_loss=0.11157  test_loss=0.13726  test_cos=0.8627  lr=1.00e-03
20:14:30 [INFO] [ada-002_to_bge-m3][deep] 13/15  train_loss=0.11138  test_loss=0.13656  test_cos=0.8634  lr=1.00e-03
20:14:41 [INFO] [ada-002_to_bge-m3][deep] 14/15  train_loss=0.11121  test_loss=0.13593  test_cos=0.8641  lr=1.00e-03
20:14:52 [INFO] [ada-002_to_bge-m3][deep] 15/15  train_loss=0.11106  test_loss=0.13534  test_cos=0.8647  lr=1.00e-03
20:14:52 [INFO] [ada-002_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8668 saved → ada-002_to_bge-m3.pt  (341.6s)
20:14:52 [INFO]
─── [4/49] ada-002 → me5-large ───
20:14:52 [INFO] [ada-002_to_me5-large] 1536d → 1024d
20:15:04 [INFO] [ada-002_to_me5-large][linear] 01/15  train_loss=0.05224  test_loss=0.06859  test_cos=0.9314  lr=1.00e-03
20:15:16 [INFO] [ada-002_to_me5-large][linear] 02/15  train_loss=0.04575  test_loss=0.06461  test_cos=0.9354  lr=1.00e-03
20:15:28 [INFO] [ada-002_to_me5-large][linear] 03/15  train_loss=0.04500  test_loss=0.06231  test_cos=0.9377  lr=1.00e-03
20:15:40 [INFO] [ada-002_to_me5-large][linear] 04/15  train_loss=0.04460  test_loss=0.06073  test_cos=0.9393  lr=1.00e-03
20:15:52 [INFO] [ada-002_to_me5-large][linear] 05/15  train_loss=0.04433  test_loss=0.05966  test_cos=0.9403  lr=1.00e-03
20:16:04 [INFO] [ada-002_to_me5-large][linear] 06/15  train_loss=0.04413  test_loss=0.05893  test_cos=0.9411  lr=1.00e-03
20:16:16 [INFO] [ada-002_to_me5-large][linear] 07/15  train_loss=0.04398  test_loss=0.05844  test_cos=0.9416  lr=1.00e-03
20:16:28 [INFO] [ada-002_to_me5-large][linear] 08/15  train_loss=0.04386  test_loss=0.05810  test_cos=0.9419  lr=1.00e-03
20:16:40 [INFO] [ada-002_to_me5-large][linear] 09/15  train_loss=0.04376  test_loss=0.05785  test_cos=0.9421  lr=1.00e-03
20:16:52 [INFO] [ada-002_to_me5-large][linear] 10/15  train_loss=0.04368  test_loss=0.05765  test_cos=0.9424  lr=1.00e-03
20:17:04 [INFO] [ada-002_to_me5-large][linear] 11/15  train_loss=0.04361  test_loss=0.05746  test_cos=0.9425  lr=1.00e-03
20:17:16 [INFO] [ada-002_to_me5-large][linear] 12/15  train_loss=0.04354  test_loss=0.05729  test_cos=0.9427  lr=1.00e-03
20:17:28 [INFO] [ada-002_to_me5-large][linear] 13/15  train_loss=0.04349  test_loss=0.05712  test_cos=0.9429  lr=1.00e-03
20:17:40 [INFO] [ada-002_to_me5-large][linear] 14/15  train_loss=0.04344  test_loss=0.05695  test_cos=0.9431  lr=1.00e-03
20:17:52 [INFO] [ada-002_to_me5-large][linear] 15/15  train_loss=0.04339  test_loss=0.05677  test_cos=0.9432  lr=1.00e-03
20:18:03 [INFO] [ada-002_to_me5-large][deep] 01/15  train_loss=0.05927  test_loss=0.07557  test_cos=0.9244  lr=1.00e-03
20:18:14 [INFO] [ada-002_to_me5-large][deep] 02/15  train_loss=0.04700  test_loss=0.06971  test_cos=0.9303  lr=1.00e-03
20:18:25 [INFO] [ada-002_to_me5-large][deep] 03/15  train_loss=0.04582  test_loss=0.06747  test_cos=0.9325  lr=1.00e-03
20:18:36 [INFO] [ada-002_to_me5-large][deep] 04/15  train_loss=0.04524  test_loss=0.06552  test_cos=0.9345  lr=1.00e-03
20:18:47 [INFO] [ada-002_to_me5-large][deep] 05/15  train_loss=0.04484  test_loss=0.06394  test_cos=0.9361  lr=1.00e-03
20:18:58 [INFO] [ada-002_to_me5-large][deep] 06/15  train_loss=0.04459  test_loss=0.06283  test_cos=0.9372  lr=1.00e-03
20:19:09 [INFO] [ada-002_to_me5-large][deep] 07/15  train_loss=0.04440  test_loss=0.06203  test_cos=0.9380  lr=1.00e-03
20:19:20 [INFO] [ada-002_to_me5-large][deep] 08/15  train_loss=0.04425  test_loss=0.06143  test_cos=0.9386  lr=1.00e-03
20:19:30 [INFO] [ada-002_to_me5-large][deep] 09/15  train_loss=0.04413  test_loss=0.06095  test_cos=0.9390  lr=1.00e-03
20:19:42 [INFO] [ada-002_to_me5-large][deep] 10/15  train_loss=0.04402  test_loss=0.06046  test_cos=0.9395  lr=1.00e-03
20:19:53 [INFO] [ada-002_to_me5-large][deep] 11/15  train_loss=0.04393  test_loss=0.06005  test_cos=0.9400  lr=1.00e-03
20:20:03 [INFO] [ada-002_to_me5-large][deep] 12/15  train_loss=0.04386  test_loss=0.05964  test_cos=0.9404  lr=1.00e-03
20:20:14 [INFO] [ada-002_to_me5-large][deep] 13/15  train_loss=0.04379  test_loss=0.05924  test_cos=0.9408  lr=1.00e-03
20:20:25 [INFO] [ada-002_to_me5-large][deep] 14/15  train_loss=0.04373  test_loss=0.05878  test_cos=0.9412  lr=1.00e-03
20:20:36 [INFO] [ada-002_to_me5-large][deep] 15/15  train_loss=0.04368  test_loss=0.05834  test_cos=0.9417  lr=1.00e-03
20:20:36 [INFO] [ada-002_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9432 saved → ada-002_to_me5-large.pt  (344.4s)
20:20:36 [INFO]
─── [5/49] ada-002 → pplx-embed-1 ───
20:20:36 [INFO] [ada-002_to_pplx-embed-1] 1536d → 1024d
20:20:48 [INFO] [ada-002_to_pplx-embed-1][linear] 01/15  train_loss=0.21184  test_loss=0.29445  test_cos=0.7056  lr=1.00e-03
20:21:00 [INFO] [ada-002_to_pplx-embed-1][linear] 02/15  train_loss=0.19128  test_loss=0.27492  test_cos=0.7251  lr=1.00e-03
20:21:12 [INFO] [ada-002_to_pplx-embed-1][linear] 03/15  train_loss=0.18805  test_loss=0.26504  test_cos=0.7350  lr=1.00e-03
20:21:23 [INFO] [ada-002_to_pplx-embed-1][linear] 04/15  train_loss=0.18634  test_loss=0.25841  test_cos=0.7416  lr=1.00e-03
20:21:35 [INFO] [ada-002_to_pplx-embed-1][linear] 05/15  train_loss=0.18520  test_loss=0.25349  test_cos=0.7465  lr=1.00e-03
20:21:46 [INFO] [ada-002_to_pplx-embed-1][linear] 06/15  train_loss=0.18436  test_loss=0.24972  test_cos=0.7503  lr=1.00e-03
20:21:58 [INFO] [ada-002_to_pplx-embed-1][linear] 07/15  train_loss=0.18370  test_loss=0.24677  test_cos=0.7532  lr=1.00e-03
20:22:09 [INFO] [ada-002_to_pplx-embed-1][linear] 08/15  train_loss=0.18318  test_loss=0.24437  test_cos=0.7556  lr=1.00e-03
20:22:21 [INFO] [ada-002_to_pplx-embed-1][linear] 09/15  train_loss=0.18275  test_loss=0.24233  test_cos=0.7577  lr=1.00e-03
20:22:32 [INFO] [ada-002_to_pplx-embed-1][linear] 10/15  train_loss=0.18238  test_loss=0.24055  test_cos=0.7594  lr=1.00e-03
20:22:44 [INFO] [ada-002_to_pplx-embed-1][linear] 11/15  train_loss=0.18207  test_loss=0.23894  test_cos=0.7611  lr=1.00e-03
20:22:55 [INFO] [ada-002_to_pplx-embed-1][linear] 12/15  train_loss=0.18180  test_loss=0.23745  test_cos=0.7626  lr=1.00e-03
20:23:07 [INFO] [ada-002_to_pplx-embed-1][linear] 13/15  train_loss=0.18156  test_loss=0.23605  test_cos=0.7640  lr=1.00e-03
20:23:18 [INFO] [ada-002_to_pplx-embed-1][linear] 14/15  train_loss=0.18134  test_loss=0.23472  test_cos=0.7653  lr=1.00e-03
20:23:29 [INFO] [ada-002_to_pplx-embed-1][linear] 15/15  train_loss=0.18115  test_loss=0.23345  test_cos=0.7665  lr=1.00e-03
20:23:40 [INFO] [ada-002_to_pplx-embed-1][deep] 01/15  train_loss=0.23512  test_loss=0.32695  test_cos=0.6731  lr=1.00e-03
20:23:50 [INFO] [ada-002_to_pplx-embed-1][deep] 02/15  train_loss=0.19786  test_loss=0.29673  test_cos=0.7033  lr=1.00e-03
20:24:01 [INFO] [ada-002_to_pplx-embed-1][deep] 03/15  train_loss=0.19301  test_loss=0.28369  test_cos=0.7163  lr=1.00e-03
20:24:12 [INFO] [ada-002_to_pplx-embed-1][deep] 04/15  train_loss=0.19069  test_loss=0.27491  test_cos=0.7251  lr=1.00e-03
20:24:22 [INFO] [ada-002_to_pplx-embed-1][deep] 05/15  train_loss=0.18928  test_loss=0.26822  test_cos=0.7318  lr=1.00e-03
20:24:32 [INFO] [ada-002_to_pplx-embed-1][deep] 06/15  train_loss=0.18830  test_loss=0.26294  test_cos=0.7371  lr=1.00e-03
20:24:43 [INFO] [ada-002_to_pplx-embed-1][deep] 07/15  train_loss=0.18754  test_loss=0.25876  test_cos=0.7412  lr=1.00e-03
20:24:53 [INFO] [ada-002_to_pplx-embed-1][deep] 08/15  train_loss=0.18691  test_loss=0.25541  test_cos=0.7446  lr=1.00e-03
20:25:04 [INFO] [ada-002_to_pplx-embed-1][deep] 09/15  train_loss=0.18638  test_loss=0.25249  test_cos=0.7475  lr=1.00e-03
20:25:15 [INFO] [ada-002_to_pplx-embed-1][deep] 10/15  train_loss=0.18593  test_loss=0.24978  test_cos=0.7502  lr=1.00e-03
20:25:25 [INFO] [ada-002_to_pplx-embed-1][deep] 11/15  train_loss=0.18553  test_loss=0.24723  test_cos=0.7528  lr=1.00e-03
20:25:36 [INFO] [ada-002_to_pplx-embed-1][deep] 12/15  train_loss=0.18517  test_loss=0.24485  test_cos=0.7551  lr=1.00e-03
20:25:46 [INFO] [ada-002_to_pplx-embed-1][deep] 13/15  train_loss=0.18483  test_loss=0.24264  test_cos=0.7574  lr=1.00e-03
20:25:57 [INFO] [ada-002_to_pplx-embed-1][deep] 14/15  train_loss=0.18451  test_loss=0.24059  test_cos=0.7594  lr=1.00e-03
20:26:09 [INFO] [ada-002_to_pplx-embed-1][deep] 15/15  train_loss=0.18420  test_loss=0.23869  test_cos=0.7613  lr=1.00e-03
20:26:09 [INFO] [ada-002_to_pplx-embed-1] winner=linear best_epoch=15 best_test_cos=0.7665 saved → ada-002_to_pplx-embed-1.pt  (332.5s)
20:26:09 [INFO]
─── [6/49] ada-002 → nemotron-1b-free ───
20:26:09 [INFO] [ada-002_to_nemotron-1b-free] 1536d → 2048d
20:26:29 [INFO] [ada-002_to_nemotron-1b-free][linear] 01/15  train_loss=0.26304  test_loss=0.33392  test_cos=0.6661  lr=1.00e-03
20:26:49 [INFO] [ada-002_to_nemotron-1b-free][linear] 02/15  train_loss=0.23457  test_loss=0.31457  test_cos=0.6854  lr=1.00e-03
20:27:10 [INFO] [ada-002_to_nemotron-1b-free][linear] 03/15  train_loss=0.23045  test_loss=0.30472  test_cos=0.6953  lr=1.00e-03
20:27:31 [INFO] [ada-002_to_nemotron-1b-free][linear] 04/15  train_loss=0.22826  test_loss=0.29797  test_cos=0.7020  lr=1.00e-03
20:27:53 [INFO] [ada-002_to_nemotron-1b-free][linear] 05/15  train_loss=0.22681  test_loss=0.29288  test_cos=0.7071  lr=1.00e-03
20:28:13 [INFO] [ada-002_to_nemotron-1b-free][linear] 06/15  train_loss=0.22576  test_loss=0.28888  test_cos=0.7111  lr=1.00e-03
20:28:34 [INFO] [ada-002_to_nemotron-1b-free][linear] 07/15  train_loss=0.22494  test_loss=0.28567  test_cos=0.7143  lr=1.00e-03
20:28:55 [INFO] [ada-002_to_nemotron-1b-free][linear] 08/15  train_loss=0.22429  test_loss=0.28306  test_cos=0.7169  lr=1.00e-03
20:29:16 [INFO] [ada-002_to_nemotron-1b-free][linear] 09/15  train_loss=0.22375  test_loss=0.28089  test_cos=0.7191  lr=1.00e-03
20:29:36 [INFO] [ada-002_to_nemotron-1b-free][linear] 10/15  train_loss=0.22329  test_loss=0.27908  test_cos=0.7209  lr=1.00e-03
20:29:57 [INFO] [ada-002_to_nemotron-1b-free][linear] 11/15  train_loss=0.22290  test_loss=0.27753  test_cos=0.7225  lr=1.00e-03
20:30:18 [INFO] [ada-002_to_nemotron-1b-free][linear] 12/15  train_loss=0.22256  test_loss=0.27619  test_cos=0.7238  lr=1.00e-03
20:30:39 [INFO] [ada-002_to_nemotron-1b-free][linear] 13/15  train_loss=0.22226  test_loss=0.27499  test_cos=0.7250  lr=1.00e-03
20:31:00 [INFO] [ada-002_to_nemotron-1b-free][linear] 14/15  train_loss=0.22199  test_loss=0.27392  test_cos=0.7261  lr=1.00e-03
20:31:20 [INFO] [ada-002_to_nemotron-1b-free][linear] 15/15  train_loss=0.22175  test_loss=0.27293  test_cos=0.7271  lr=1.00e-03
20:31:40 [INFO] [ada-002_to_nemotron-1b-free][deep] 01/15  train_loss=0.29437  test_loss=0.36273  test_cos=0.6373  lr=1.00e-03
20:31:59 [INFO] [ada-002_to_nemotron-1b-free][deep] 02/15  train_loss=0.24281  test_loss=0.33062  test_cos=0.6694  lr=1.00e-03
20:32:18 [INFO] [ada-002_to_nemotron-1b-free][deep] 03/15  train_loss=0.23623  test_loss=0.31744  test_cos=0.6826  lr=1.00e-03
20:32:37 [INFO] [ada-002_to_nemotron-1b-free][deep] 04/15  train_loss=0.23295  test_loss=0.30932  test_cos=0.6907  lr=1.00e-03
20:32:56 [INFO] [ada-002_to_nemotron-1b-free][deep] 05/15  train_loss=0.23089  test_loss=0.30431  test_cos=0.6957  lr=1.00e-03
20:33:15 [INFO] [ada-002_to_nemotron-1b-free][deep] 06/15  train_loss=0.22950  test_loss=0.29991  test_cos=0.7001  lr=1.00e-03
20:33:34 [INFO] [ada-002_to_nemotron-1b-free][deep] 07/15  train_loss=0.22848  test_loss=0.29622  test_cos=0.7038  lr=1.00e-03
20:33:53 [INFO] [ada-002_to_nemotron-1b-free][deep] 08/15  train_loss=0.22768  test_loss=0.29284  test_cos=0.7072  lr=1.00e-03
20:34:13 [INFO] [ada-002_to_nemotron-1b-free][deep] 09/15  train_loss=0.22704  test_loss=0.28996  test_cos=0.7100  lr=1.00e-03
20:34:32 [INFO] [ada-002_to_nemotron-1b-free][deep] 10/15  train_loss=0.22651  test_loss=0.28757  test_cos=0.7124  lr=1.00e-03
20:34:51 [INFO] [ada-002_to_nemotron-1b-free][deep] 11/15  train_loss=0.22606  test_loss=0.28556  test_cos=0.7144  lr=1.00e-03
20:35:10 [INFO] [ada-002_to_nemotron-1b-free][deep] 12/15  train_loss=0.22567  test_loss=0.28368  test_cos=0.7163  lr=1.00e-03
20:35:30 [INFO] [ada-002_to_nemotron-1b-free][deep] 13/15  train_loss=0.22532  test_loss=0.28187  test_cos=0.7181  lr=1.00e-03
20:35:49 [INFO] [ada-002_to_nemotron-1b-free][deep] 14/15  train_loss=0.22501  test_loss=0.28018  test_cos=0.7198  lr=1.00e-03
20:36:08 [INFO] [ada-002_to_nemotron-1b-free][deep] 15/15  train_loss=0.22474  test_loss=0.27868  test_cos=0.7213  lr=1.00e-03
20:36:08 [INFO] [ada-002_to_nemotron-1b-free] winner=linear best_epoch=15 best_test_cos=0.7271 saved → ada-002_to_nemotron-1b-free.pt  (599.4s)
20:36:08 [INFO]
─── [7/49] ada-002 → fastembed-bge-small ───
20:36:08 [INFO] [ada-002_to_fastembed-bge-small] 1536d → 384d
20:36:16 [INFO] [ada-002_to_fastembed-bge-small][linear] 01/15  train_loss=0.07991  test_loss=0.12221  test_cos=0.8778  lr=1.00e-03
20:36:22 [INFO] [ada-002_to_fastembed-bge-small][linear] 02/15  train_loss=0.07299  test_loss=0.11356  test_cos=0.8864  lr=1.00e-03
20:36:29 [INFO] [ada-002_to_fastembed-bge-small][linear] 03/15  train_loss=0.07185  test_loss=0.10892  test_cos=0.8911  lr=1.00e-03
20:36:36 [INFO] [ada-002_to_fastembed-bge-small][linear] 04/15  train_loss=0.07124  test_loss=0.10604  test_cos=0.8940  lr=1.00e-03
20:36:43 [INFO] [ada-002_to_fastembed-bge-small][linear] 05/15  train_loss=0.07082  test_loss=0.10410  test_cos=0.8959  lr=1.00e-03
20:36:50 [INFO] [ada-002_to_fastembed-bge-small][linear] 06/15  train_loss=0.07051  test_loss=0.10274  test_cos=0.8973  lr=1.00e-03
20:36:57 [INFO] [ada-002_to_fastembed-bge-small][linear] 07/15  train_loss=0.07027  test_loss=0.10171  test_cos=0.8983  lr=1.00e-03
20:37:04 [INFO] [ada-002_to_fastembed-bge-small][linear] 08/15  train_loss=0.07008  test_loss=0.10086  test_cos=0.8991  lr=1.00e-03
20:37:11 [INFO] [ada-002_to_fastembed-bge-small][linear] 09/15  train_loss=0.06992  test_loss=0.10009  test_cos=0.8999  lr=1.00e-03
20:37:18 [INFO] [ada-002_to_fastembed-bge-small][linear] 10/15  train_loss=0.06978  test_loss=0.09938  test_cos=0.9006  lr=1.00e-03
20:37:25 [INFO] [ada-002_to_fastembed-bge-small][linear] 11/15  train_loss=0.06967  test_loss=0.09869  test_cos=0.9013  lr=1.00e-03
20:37:32 [INFO] [ada-002_to_fastembed-bge-small][linear] 12/15  train_loss=0.06957  test_loss=0.09803  test_cos=0.9020  lr=1.00e-03
20:37:39 [INFO] [ada-002_to_fastembed-bge-small][linear] 13/15  train_loss=0.06948  test_loss=0.09738  test_cos=0.9026  lr=1.00e-03
20:37:46 [INFO] [ada-002_to_fastembed-bge-small][linear] 14/15  train_loss=0.06940  test_loss=0.09674  test_cos=0.9033  lr=1.00e-03
20:37:53 [INFO] [ada-002_to_fastembed-bge-small][linear] 15/15  train_loss=0.06933  test_loss=0.09613  test_cos=0.9039  lr=1.00e-03
20:37:59 [INFO] [ada-002_to_fastembed-bge-small][deep] 01/15  train_loss=0.09770  test_loss=0.14238  test_cos=0.8576  lr=1.00e-03
20:38:05 [INFO] [ada-002_to_fastembed-bge-small][deep] 02/15  train_loss=0.07977  test_loss=0.12604  test_cos=0.8740  lr=1.00e-03
20:38:12 [INFO] [ada-002_to_fastembed-bge-small][deep] 03/15  train_loss=0.07798  test_loss=0.12047  test_cos=0.8795  lr=1.00e-03
20:38:18 [INFO] [ada-002_to_fastembed-bge-small][deep] 04/15  train_loss=0.07723  test_loss=0.11709  test_cos=0.8829  lr=1.00e-03
20:38:24 [INFO] [ada-002_to_fastembed-bge-small][deep] 05/15  train_loss=0.07680  test_loss=0.11473  test_cos=0.8853  lr=1.00e-03
20:38:30 [INFO] [ada-002_to_fastembed-bge-small][deep] 06/15  train_loss=0.07653  test_loss=0.11292  test_cos=0.8871  lr=1.00e-03
20:38:36 [INFO] [ada-002_to_fastembed-bge-small][deep] 07/15  train_loss=0.07631  test_loss=0.11076  test_cos=0.8892  lr=1.00e-03
20:38:42 [INFO] [ada-002_to_fastembed-bge-small][deep] 08/15  train_loss=0.07612  test_loss=0.10896  test_cos=0.8910  lr=1.00e-03
20:38:48 [INFO] [ada-002_to_fastembed-bge-small][deep] 09/15  train_loss=0.07598  test_loss=0.10753  test_cos=0.8925  lr=1.00e-03
20:38:54 [INFO] [ada-002_to_fastembed-bge-small][deep] 10/15  train_loss=0.07585  test_loss=0.10638  test_cos=0.8936  lr=1.00e-03
20:39:00 [INFO] [ada-002_to_fastembed-bge-small][deep] 11/15  train_loss=0.07575  test_loss=0.10545  test_cos=0.8946  lr=1.00e-03
20:39:06 [INFO] [ada-002_to_fastembed-bge-small][deep] 12/15  train_loss=0.07565  test_loss=0.10466  test_cos=0.8953  lr=1.00e-03
20:39:13 [INFO] [ada-002_to_fastembed-bge-small][deep] 13/15  train_loss=0.07557  test_loss=0.10397  test_cos=0.8960  lr=1.00e-03
20:39:19 [INFO] [ada-002_to_fastembed-bge-small][deep] 14/15  train_loss=0.07550  test_loss=0.10332  test_cos=0.8967  lr=1.00e-03
20:39:25 [INFO] [ada-002_to_fastembed-bge-small][deep] 15/15  train_loss=0.07543  test_loss=0.10270  test_cos=0.8973  lr=1.00e-03
20:39:25 [INFO] [ada-002_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.9039 saved → ada-002_to_fastembed-bge-small.pt  (196.4s)
20:39:25 [INFO]
─── [8/49] te3-small → qwen3-emb-8b ───
20:39:25 [INFO] [te3-small_to_qwen3-emb-8b] 1536d → 4096d
20:40:05 [INFO] [te3-small_to_qwen3-emb-8b][linear] 01/15  train_loss=0.16217  test_loss=0.25656  test_cos=0.7434  lr=1.00e-03
20:40:47 [INFO] [te3-small_to_qwen3-emb-8b][linear] 02/15  train_loss=0.14675  test_loss=0.23587  test_cos=0.7641  lr=1.00e-03
20:41:28 [INFO] [te3-small_to_qwen3-emb-8b][linear] 03/15  train_loss=0.14445  test_loss=0.22524  test_cos=0.7748  lr=1.00e-03
20:42:10 [INFO] [te3-small_to_qwen3-emb-8b][linear] 04/15  train_loss=0.14334  test_loss=0.21783  test_cos=0.7822  lr=1.00e-03
20:42:51 [INFO] [te3-small_to_qwen3-emb-8b][linear] 05/15  train_loss=0.14265  test_loss=0.21218  test_cos=0.7878  lr=1.00e-03
20:43:33 [INFO] [te3-small_to_qwen3-emb-8b][linear] 06/15  train_loss=0.14218  test_loss=0.20771  test_cos=0.7923  lr=1.00e-03
20:44:15 [INFO] [te3-small_to_qwen3-emb-8b][linear] 07/15  train_loss=0.14183  test_loss=0.20405  test_cos=0.7959  lr=1.00e-03
20:44:57 [INFO] [te3-small_to_qwen3-emb-8b][linear] 08/15  train_loss=0.14156  test_loss=0.20099  test_cos=0.7990  lr=1.00e-03
20:45:38 [INFO] [te3-small_to_qwen3-emb-8b][linear] 09/15  train_loss=0.14135  test_loss=0.19838  test_cos=0.8016  lr=1.00e-03
20:46:21 [INFO] [te3-small_to_qwen3-emb-8b][linear] 10/15  train_loss=0.14117  test_loss=0.19611  test_cos=0.8039  lr=1.00e-03
20:47:01 [INFO] [te3-small_to_qwen3-emb-8b][linear] 11/15  train_loss=0.14103  test_loss=0.19411  test_cos=0.8059  lr=1.00e-03
20:47:41 [INFO] [te3-small_to_qwen3-emb-8b][linear] 12/15  train_loss=0.14091  test_loss=0.19233  test_cos=0.8077  lr=1.00e-03
20:48:21 [INFO] [te3-small_to_qwen3-emb-8b][linear] 13/15  train_loss=0.14081  test_loss=0.19072  test_cos=0.8093  lr=1.00e-03
20:49:01 [INFO] [te3-small_to_qwen3-emb-8b][linear] 14/15  train_loss=0.14071  test_loss=0.18927  test_cos=0.8107  lr=1.00e-03
20:49:41 [INFO] [te3-small_to_qwen3-emb-8b][linear] 15/15  train_loss=0.14064  test_loss=0.18794  test_cos=0.8121  lr=1.00e-03
20:50:13 [INFO] [te3-small_to_qwen3-emb-8b][deep] 01/15  train_loss=0.18609  test_loss=0.28204  test_cos=0.7180  lr=1.00e-03
20:50:45 [INFO] [te3-small_to_qwen3-emb-8b][deep] 02/15  train_loss=0.15338  test_loss=0.25242  test_cos=0.7476  lr=1.00e-03
20:51:18 [INFO] [te3-small_to_qwen3-emb-8b][deep] 03/15  train_loss=0.14886  test_loss=0.24014  test_cos=0.7599  lr=1.00e-03
20:51:50 [INFO] [te3-small_to_qwen3-emb-8b][deep] 04/15  train_loss=0.14660  test_loss=0.23270  test_cos=0.7673  lr=1.00e-03
20:52:23 [INFO] [te3-small_to_qwen3-emb-8b][deep] 05/15  train_loss=0.14518  test_loss=0.22634  test_cos=0.7737  lr=1.00e-03
20:52:56 [INFO] [te3-small_to_qwen3-emb-8b][deep] 06/15  train_loss=0.14415  test_loss=0.22100  test_cos=0.7790  lr=1.00e-03
20:53:28 [INFO] [te3-small_to_qwen3-emb-8b][deep] 07/15  train_loss=0.14332  test_loss=0.21610  test_cos=0.7839  lr=1.00e-03
20:54:00 [INFO] [te3-small_to_qwen3-emb-8b][deep] 08/15  train_loss=0.14260  test_loss=0.21167  test_cos=0.7883  lr=1.00e-03
20:54:33 [INFO] [te3-small_to_qwen3-emb-8b][deep] 09/15  train_loss=0.14197  test_loss=0.20770  test_cos=0.7923  lr=1.00e-03
20:55:05 [INFO] [te3-small_to_qwen3-emb-8b][deep] 10/15  train_loss=0.14139  test_loss=0.20421  test_cos=0.7958  lr=1.00e-03
20:55:39 [INFO] [te3-small_to_qwen3-emb-8b][deep] 11/15  train_loss=0.14087  test_loss=0.20099  test_cos=0.7990  lr=1.00e-03
20:56:12 [INFO] [te3-small_to_qwen3-emb-8b][deep] 12/15  train_loss=0.14038  test_loss=0.19806  test_cos=0.8019  lr=1.00e-03
20:56:45 [INFO] [te3-small_to_qwen3-emb-8b][deep] 13/15  train_loss=0.13992  test_loss=0.19539  test_cos=0.8046  lr=1.00e-03
20:57:17 [INFO] [te3-small_to_qwen3-emb-8b][deep] 14/15  train_loss=0.13948  test_loss=0.19295  test_cos=0.8071  lr=1.00e-03
20:57:49 [INFO] [te3-small_to_qwen3-emb-8b][deep] 15/15  train_loss=0.13907  test_loss=0.19072  test_cos=0.8093  lr=1.00e-03
20:57:49 [INFO] [te3-small_to_qwen3-emb-8b] winner=linear best_epoch=15 best_test_cos=0.8121 saved → te3-small_to_qwen3-emb-8b.pt  (1104.7s)
20:57:49 [INFO]
─── [9/49] te3-small → bge-m3 ───
20:57:49 [INFO] [te3-small_to_bge-m3] 1536d → 1024d
20:58:02 [INFO] [te3-small_to_bge-m3][linear] 01/15  train_loss=0.12818  test_loss=0.15776  test_cos=0.8422  lr=1.00e-03
20:58:14 [INFO] [te3-small_to_bge-m3][linear] 02/15  train_loss=0.11678  test_loss=0.14981  test_cos=0.8502  lr=1.00e-03
20:58:26 [INFO] [te3-small_to_bge-m3][linear] 03/15  train_loss=0.11524  test_loss=0.14565  test_cos=0.8543  lr=1.00e-03
20:58:38 [INFO] [te3-small_to_bge-m3][linear] 04/15  train_loss=0.11446  test_loss=0.14261  test_cos=0.8574  lr=1.00e-03
20:58:50 [INFO] [te3-small_to_bge-m3][linear] 05/15  train_loss=0.11396  test_loss=0.14021  test_cos=0.8598  lr=1.00e-03
20:59:02 [INFO] [te3-small_to_bge-m3][linear] 06/15  train_loss=0.11360  test_loss=0.13827  test_cos=0.8617  lr=1.00e-03
20:59:14 [INFO] [te3-small_to_bge-m3][linear] 07/15  train_loss=0.11332  test_loss=0.13668  test_cos=0.8633  lr=1.00e-03
20:59:25 [INFO] [te3-small_to_bge-m3][linear] 08/15  train_loss=0.11311  test_loss=0.13535  test_cos=0.8646  lr=1.00e-03
20:59:37 [INFO] [te3-small_to_bge-m3][linear] 09/15  train_loss=0.11294  test_loss=0.13422  test_cos=0.8658  lr=1.00e-03
20:59:49 [INFO] [te3-small_to_bge-m3][linear] 10/15  train_loss=0.11280  test_loss=0.13324  test_cos=0.8668  lr=1.00e-03
21:00:01 [INFO] [te3-small_to_bge-m3][linear] 11/15  train_loss=0.11268  test_loss=0.13239  test_cos=0.8676  lr=1.00e-03
21:00:13 [INFO] [te3-small_to_bge-m3][linear] 12/15  train_loss=0.11258  test_loss=0.13163  test_cos=0.8684  lr=1.00e-03
21:00:25 [INFO] [te3-small_to_bge-m3][linear] 13/15  train_loss=0.11249  test_loss=0.13096  test_cos=0.8690  lr=1.00e-03
21:00:37 [INFO] [te3-small_to_bge-m3][linear] 14/15  train_loss=0.11241  test_loss=0.13035  test_cos=0.8696  lr=1.00e-03
21:00:49 [INFO] [te3-small_to_bge-m3][linear] 15/15  train_loss=0.11234  test_loss=0.12980  test_cos=0.8702  lr=1.00e-03
21:01:00 [INFO] [te3-small_to_bge-m3][deep] 01/15  train_loss=0.13935  test_loss=0.17351  test_cos=0.8265  lr=1.00e-03
21:01:11 [INFO] [te3-small_to_bge-m3][deep] 02/15  train_loss=0.11939  test_loss=0.16007  test_cos=0.8399  lr=1.00e-03
21:01:22 [INFO] [te3-small_to_bge-m3][deep] 03/15  train_loss=0.11715  test_loss=0.15410  test_cos=0.8459  lr=1.00e-03
21:01:32 [INFO] [te3-small_to_bge-m3][deep] 04/15  train_loss=0.11602  test_loss=0.15018  test_cos=0.8498  lr=1.00e-03
21:01:43 [INFO] [te3-small_to_bge-m3][deep] 05/15  train_loss=0.11529  test_loss=0.14737  test_cos=0.8526  lr=1.00e-03
21:01:54 [INFO] [te3-small_to_bge-m3][deep] 06/15  train_loss=0.11476  test_loss=0.14528  test_cos=0.8547  lr=1.00e-03
21:02:05 [INFO] [te3-small_to_bge-m3][deep] 07/15  train_loss=0.11436  test_loss=0.14354  test_cos=0.8565  lr=1.00e-03
21:02:16 [INFO] [te3-small_to_bge-m3][deep] 08/15  train_loss=0.11404  test_loss=0.14200  test_cos=0.8580  lr=1.00e-03
21:02:27 [INFO] [te3-small_to_bge-m3][deep] 09/15  train_loss=0.11377  test_loss=0.14068  test_cos=0.8593  lr=1.00e-03
21:02:37 [INFO] [te3-small_to_bge-m3][deep] 10/15  train_loss=0.11354  test_loss=0.13951  test_cos=0.8605  lr=1.00e-03
21:02:48 [INFO] [te3-small_to_bge-m3][deep] 11/15  train_loss=0.11333  test_loss=0.13848  test_cos=0.8615  lr=1.00e-03
21:02:59 [INFO] [te3-small_to_bge-m3][deep] 12/15  train_loss=0.11314  test_loss=0.13757  test_cos=0.8624  lr=1.00e-03
21:03:10 [INFO] [te3-small_to_bge-m3][deep] 13/15  train_loss=0.11297  test_loss=0.13673  test_cos=0.8633  lr=1.00e-03
21:03:21 [INFO] [te3-small_to_bge-m3][deep] 14/15  train_loss=0.11282  test_loss=0.13594  test_cos=0.8641  lr=1.00e-03
21:03:32 [INFO] [te3-small_to_bge-m3][deep] 15/15  train_loss=0.11267  test_loss=0.13521  test_cos=0.8648  lr=1.00e-03
21:03:32 [INFO] [te3-small_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8702 saved → te3-small_to_bge-m3.pt  (342.2s)
21:03:32 [INFO]
─── [10/49] te3-small → me5-large ───
21:03:32 [INFO] [te3-small_to_me5-large] 1536d → 1024d
21:03:44 [INFO] [te3-small_to_me5-large][linear] 01/15  train_loss=0.05180  test_loss=0.06643  test_cos=0.9336  lr=1.00e-03
21:03:56 [INFO] [te3-small_to_me5-large][linear] 02/15  train_loss=0.04584  test_loss=0.06298  test_cos=0.9370  lr=1.00e-03
21:04:08 [INFO] [te3-small_to_me5-large][linear] 03/15  train_loss=0.04511  test_loss=0.06116  test_cos=0.9388  lr=1.00e-03
21:04:20 [INFO] [te3-small_to_me5-large][linear] 04/15  train_loss=0.04476  test_loss=0.05979  test_cos=0.9402  lr=1.00e-03
21:04:32 [INFO] [te3-small_to_me5-large][linear] 05/15  train_loss=0.04454  test_loss=0.05871  test_cos=0.9413  lr=1.00e-03
21:04:44 [INFO] [te3-small_to_me5-large][linear] 06/15  train_loss=0.04438  test_loss=0.05783  test_cos=0.9422  lr=1.00e-03
21:04:56 [INFO] [te3-small_to_me5-large][linear] 07/15  train_loss=0.04426  test_loss=0.05710  test_cos=0.9429  lr=1.00e-03
21:05:08 [INFO] [te3-small_to_me5-large][linear] 08/15  train_loss=0.04417  test_loss=0.05648  test_cos=0.9435  lr=1.00e-03
21:05:20 [INFO] [te3-small_to_me5-large][linear] 09/15  train_loss=0.04410  test_loss=0.05595  test_cos=0.9440  lr=1.00e-03
21:05:32 [INFO] [te3-small_to_me5-large][linear] 10/15  train_loss=0.04403  test_loss=0.05549  test_cos=0.9445  lr=1.00e-03
21:05:44 [INFO] [te3-small_to_me5-large][linear] 11/15  train_loss=0.04398  test_loss=0.05510  test_cos=0.9449  lr=1.00e-03
21:05:56 [INFO] [te3-small_to_me5-large][linear] 12/15  train_loss=0.04394  test_loss=0.05475  test_cos=0.9453  lr=1.00e-03
21:06:08 [INFO] [te3-small_to_me5-large][linear] 13/15  train_loss=0.04390  test_loss=0.05444  test_cos=0.9456  lr=1.00e-03
21:06:20 [INFO] [te3-small_to_me5-large][linear] 14/15  train_loss=0.04387  test_loss=0.05416  test_cos=0.9458  lr=1.00e-03
21:06:32 [INFO] [te3-small_to_me5-large][linear] 15/15  train_loss=0.04384  test_loss=0.05391  test_cos=0.9461  lr=1.00e-03
21:06:43 [INFO] [te3-small_to_me5-large][deep] 01/15  train_loss=0.05723  test_loss=0.07749  test_cos=0.9225  lr=1.00e-03
21:06:54 [INFO] [te3-small_to_me5-large][deep] 02/15  train_loss=0.04704  test_loss=0.07041  test_cos=0.9296  lr=1.00e-03
21:07:04 [INFO] [te3-small_to_me5-large][deep] 03/15  train_loss=0.04601  test_loss=0.06690  test_cos=0.9331  lr=1.00e-03
21:07:15 [INFO] [te3-small_to_me5-large][deep] 04/15  train_loss=0.04551  test_loss=0.06461  test_cos=0.9354  lr=1.00e-03
21:07:26 [INFO] [te3-small_to_me5-large][deep] 05/15  train_loss=0.04520  test_loss=0.06297  test_cos=0.9370  lr=1.00e-03
21:07:37 [INFO] [te3-small_to_me5-large][deep] 06/15  train_loss=0.04498  test_loss=0.06168  test_cos=0.9383  lr=1.00e-03
21:07:48 [INFO] [te3-small_to_me5-large][deep] 07/15  train_loss=0.04482  test_loss=0.06069  test_cos=0.9393  lr=1.00e-03
21:07:59 [INFO] [te3-small_to_me5-large][deep] 08/15  train_loss=0.04469  test_loss=0.05983  test_cos=0.9402  lr=1.00e-03
21:08:10 [INFO] [te3-small_to_me5-large][deep] 09/15  train_loss=0.04458  test_loss=0.05917  test_cos=0.9408  lr=1.00e-03
21:08:21 [INFO] [te3-small_to_me5-large][deep] 10/15  train_loss=0.04450  test_loss=0.05854  test_cos=0.9415  lr=1.00e-03
21:08:31 [INFO] [te3-small_to_me5-large][deep] 11/15  train_loss=0.04442  test_loss=0.05805  test_cos=0.9419  lr=1.00e-03
21:08:42 [INFO] [te3-small_to_me5-large][deep] 12/15  train_loss=0.04436  test_loss=0.05758  test_cos=0.9424  lr=1.00e-03
21:08:53 [INFO] [te3-small_to_me5-large][deep] 13/15  train_loss=0.04430  test_loss=0.05719  test_cos=0.9428  lr=1.00e-03
21:09:04 [INFO] [te3-small_to_me5-large][deep] 14/15  train_loss=0.04425  test_loss=0.05682  test_cos=0.9432  lr=1.00e-03
21:09:15 [INFO] [te3-small_to_me5-large][deep] 15/15  train_loss=0.04420  test_loss=0.05651  test_cos=0.9435  lr=1.00e-03
21:09:15 [INFO] [te3-small_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9461 saved → te3-small_to_me5-large.pt  (343.6s)
21:09:15 [INFO]
─── [11/49] te3-small → pplx-embed-1 ───
21:09:15 [INFO] [te3-small_to_pplx-embed-1] 1536d → 1024d
21:09:27 [INFO] [te3-small_to_pplx-embed-1][linear] 01/15  train_loss=0.20285  test_loss=0.29149  test_cos=0.7085  lr=1.00e-03
21:09:39 [INFO] [te3-small_to_pplx-embed-1][linear] 02/15  train_loss=0.18654  test_loss=0.27063  test_cos=0.7294  lr=1.00e-03
21:09:51 [INFO] [te3-small_to_pplx-embed-1][linear] 03/15  train_loss=0.18389  test_loss=0.25992  test_cos=0.7401  lr=1.00e-03
21:10:03 [INFO] [te3-small_to_pplx-embed-1][linear] 04/15  train_loss=0.18258  test_loss=0.25249  test_cos=0.7475  lr=1.00e-03
21:10:15 [INFO] [te3-small_to_pplx-embed-1][linear] 05/15  train_loss=0.18174  test_loss=0.24682  test_cos=0.7532  lr=1.00e-03
21:10:27 [INFO] [te3-small_to_pplx-embed-1][linear] 06/15  train_loss=0.18114  test_loss=0.24226  test_cos=0.7577  lr=1.00e-03
21:10:39 [INFO] [te3-small_to_pplx-embed-1][linear] 07/15  train_loss=0.18069  test_loss=0.23848  test_cos=0.7615  lr=1.00e-03
21:10:51 [INFO] [te3-small_to_pplx-embed-1][linear] 08/15  train_loss=0.18034  test_loss=0.23527  test_cos=0.7647  lr=1.00e-03
21:11:03 [INFO] [te3-small_to_pplx-embed-1][linear] 09/15  train_loss=0.18006  test_loss=0.23251  test_cos=0.7675  lr=1.00e-03
21:11:15 [INFO] [te3-small_to_pplx-embed-1][linear] 10/15  train_loss=0.17983  test_loss=0.23011  test_cos=0.7699  lr=1.00e-03
21:11:27 [INFO] [te3-small_to_pplx-embed-1][linear] 11/15  train_loss=0.17963  test_loss=0.22799  test_cos=0.7720  lr=1.00e-03
21:11:39 [INFO] [te3-small_to_pplx-embed-1][linear] 12/15  train_loss=0.17947  test_loss=0.22611  test_cos=0.7739  lr=1.00e-03
21:11:51 [INFO] [te3-small_to_pplx-embed-1][linear] 13/15  train_loss=0.17932  test_loss=0.22443  test_cos=0.7756  lr=1.00e-03
21:12:03 [INFO] [te3-small_to_pplx-embed-1][linear] 14/15  train_loss=0.17920  test_loss=0.22291  test_cos=0.7771  lr=1.00e-03
21:12:15 [INFO] [te3-small_to_pplx-embed-1][linear] 15/15  train_loss=0.17909  test_loss=0.22154  test_cos=0.7785  lr=1.00e-03
21:12:25 [INFO] [te3-small_to_pplx-embed-1][deep] 01/15  train_loss=0.22313  test_loss=0.31848  test_cos=0.6815  lr=1.00e-03
21:12:36 [INFO] [te3-small_to_pplx-embed-1][deep] 02/15  train_loss=0.19414  test_loss=0.29116  test_cos=0.7088  lr=1.00e-03
21:12:47 [INFO] [te3-small_to_pplx-embed-1][deep] 03/15  train_loss=0.19023  test_loss=0.27795  test_cos=0.7220  lr=1.00e-03
21:12:58 [INFO] [te3-small_to_pplx-embed-1][deep] 04/15  train_loss=0.18842  test_loss=0.26906  test_cos=0.7309  lr=1.00e-03
21:13:09 [INFO] [te3-small_to_pplx-embed-1][deep] 05/15  train_loss=0.18732  test_loss=0.26256  test_cos=0.7374  lr=1.00e-03
21:13:20 [INFO] [te3-small_to_pplx-embed-1][deep] 06/15  train_loss=0.18653  test_loss=0.25736  test_cos=0.7426  lr=1.00e-03
21:13:30 [INFO] [te3-small_to_pplx-embed-1][deep] 07/15  train_loss=0.18591  test_loss=0.25314  test_cos=0.7469  lr=1.00e-03
21:13:41 [INFO] [te3-small_to_pplx-embed-1][deep] 08/15  train_loss=0.18540  test_loss=0.24961  test_cos=0.7504  lr=1.00e-03
21:13:52 [INFO] [te3-small_to_pplx-embed-1][deep] 09/15  train_loss=0.18496  test_loss=0.24662  test_cos=0.7534  lr=1.00e-03
21:14:03 [INFO] [te3-small_to_pplx-embed-1][deep] 10/15  train_loss=0.18457  test_loss=0.24405  test_cos=0.7560  lr=1.00e-03
21:14:14 [INFO] [te3-small_to_pplx-embed-1][deep] 11/15  train_loss=0.18421  test_loss=0.24179  test_cos=0.7582  lr=1.00e-03
21:14:25 [INFO] [te3-small_to_pplx-embed-1][deep] 12/15  train_loss=0.18388  test_loss=0.23975  test_cos=0.7602  lr=1.00e-03
21:14:35 [INFO] [te3-small_to_pplx-embed-1][deep] 13/15  train_loss=0.18356  test_loss=0.23790  test_cos=0.7621  lr=1.00e-03
21:14:46 [INFO] [te3-small_to_pplx-embed-1][deep] 14/15  train_loss=0.18325  test_loss=0.23621  test_cos=0.7638  lr=1.00e-03
21:14:57 [INFO] [te3-small_to_pplx-embed-1][deep] 15/15  train_loss=0.18296  test_loss=0.23464  test_cos=0.7654  lr=1.00e-03
21:14:57 [INFO] [te3-small_to_pplx-embed-1] winner=linear best_epoch=15 best_test_cos=0.7785 saved → te3-small_to_pplx-embed-1.pt  (341.8s)
21:14:57 [INFO]
─── [12/49] te3-small → nemotron-1b-free ───
21:14:57 [INFO] [te3-small_to_nemotron-1b-free] 1536d → 2048d
21:15:18 [INFO] [te3-small_to_nemotron-1b-free][linear] 01/15  train_loss=0.25228  test_loss=0.32513  test_cos=0.6749  lr=1.00e-03
21:15:38 [INFO] [te3-small_to_nemotron-1b-free][linear] 02/15  train_loss=0.22931  test_loss=0.30654  test_cos=0.6935  lr=1.00e-03
21:15:58 [INFO] [te3-small_to_nemotron-1b-free][linear] 03/15  train_loss=0.22607  test_loss=0.29700  test_cos=0.7030  lr=1.00e-03
21:16:19 [INFO] [te3-small_to_nemotron-1b-free][linear] 04/15  train_loss=0.22442  test_loss=0.29041  test_cos=0.7096  lr=1.00e-03
21:16:39 [INFO] [te3-small_to_nemotron-1b-free][linear] 05/15  train_loss=0.22337  test_loss=0.28534  test_cos=0.7147  lr=1.00e-03
21:17:01 [INFO] [te3-small_to_nemotron-1b-free][linear] 06/15  train_loss=0.22262  test_loss=0.28124  test_cos=0.7188  lr=1.00e-03
21:17:23 [INFO] [te3-small_to_nemotron-1b-free][linear] 07/15  train_loss=0.22205  test_loss=0.27785  test_cos=0.7221  lr=1.00e-03
21:17:46 [INFO] [te3-small_to_nemotron-1b-free][linear] 08/15  train_loss=0.22160  test_loss=0.27499  test_cos=0.7250  lr=1.00e-03
21:18:09 [INFO] [te3-small_to_nemotron-1b-free][linear] 09/15  train_loss=0.22124  test_loss=0.27253  test_cos=0.7275  lr=1.00e-03
21:18:31 [INFO] [te3-small_to_nemotron-1b-free][linear] 10/15  train_loss=0.22094  test_loss=0.27040  test_cos=0.7296  lr=1.00e-03
21:18:52 [INFO] [te3-small_to_nemotron-1b-free][linear] 11/15  train_loss=0.22069  test_loss=0.26851  test_cos=0.7315  lr=1.00e-03
21:19:13 [INFO] [te3-small_to_nemotron-1b-free][linear] 12/15  train_loss=0.22047  test_loss=0.26684  test_cos=0.7332  lr=1.00e-03
21:19:35 [INFO] [te3-small_to_nemotron-1b-free][linear] 13/15  train_loss=0.22029  test_loss=0.26534  test_cos=0.7347  lr=1.00e-03
21:19:57 [INFO] [te3-small_to_nemotron-1b-free][linear] 14/15  train_loss=0.22012  test_loss=0.26398  test_cos=0.7360  lr=1.00e-03
21:20:19 [INFO] [te3-small_to_nemotron-1b-free][linear] 15/15  train_loss=0.21998  test_loss=0.26274  test_cos=0.7373  lr=1.00e-03
21:20:39 [INFO] [te3-small_to_nemotron-1b-free][deep] 01/15  train_loss=0.27751  test_loss=0.35145  test_cos=0.6486  lr=1.00e-03
21:21:00 [INFO] [te3-small_to_nemotron-1b-free][deep] 02/15  train_loss=0.23797  test_loss=0.32369  test_cos=0.6763  lr=1.00e-03
21:21:20 [INFO] [te3-small_to_nemotron-1b-free][deep] 03/15  train_loss=0.23270  test_loss=0.31140  test_cos=0.6886  lr=1.00e-03
21:21:40 [INFO] [te3-small_to_nemotron-1b-free][deep] 04/15  train_loss=0.23011  test_loss=0.30412  test_cos=0.6959  lr=1.00e-03
21:21:59 [INFO] [te3-small_to_nemotron-1b-free][deep] 05/15  train_loss=0.22859  test_loss=0.29868  test_cos=0.7013  lr=1.00e-03
21:22:18 [INFO] [te3-small_to_nemotron-1b-free][deep] 06/15  train_loss=0.22758  test_loss=0.29435  test_cos=0.7057  lr=1.00e-03
21:22:37 [INFO] [te3-small_to_nemotron-1b-free][deep] 07/15  train_loss=0.22682  test_loss=0.29072  test_cos=0.7093  lr=1.00e-03
21:22:57 [INFO] [te3-small_to_nemotron-1b-free][deep] 08/15  train_loss=0.22624  test_loss=0.28753  test_cos=0.7125  lr=1.00e-03
21:23:16 [INFO] [te3-small_to_nemotron-1b-free][deep] 09/15  train_loss=0.22578  test_loss=0.28475  test_cos=0.7153  lr=1.00e-03
21:23:35 [INFO] [te3-small_to_nemotron-1b-free][deep] 10/15  train_loss=0.22539  test_loss=0.28230  test_cos=0.7177  lr=1.00e-03
21:23:54 [INFO] [te3-small_to_nemotron-1b-free][deep] 11/15  train_loss=0.22505  test_loss=0.28012  test_cos=0.7199  lr=1.00e-03
21:24:13 [INFO] [te3-small_to_nemotron-1b-free][deep] 12/15  train_loss=0.22475  test_loss=0.27815  test_cos=0.7218  lr=1.00e-03
21:24:32 [INFO] [te3-small_to_nemotron-1b-free][deep] 13/15  train_loss=0.22449  test_loss=0.27639  test_cos=0.7236  lr=1.00e-03
21:24:50 [INFO] [te3-small_to_nemotron-1b-free][deep] 14/15  train_loss=0.22425  test_loss=0.27480  test_cos=0.7252  lr=1.00e-03
21:25:09 [INFO] [te3-small_to_nemotron-1b-free][deep] 15/15  train_loss=0.22403  test_loss=0.27334  test_cos=0.7267  lr=1.00e-03
21:25:09 [INFO] [te3-small_to_nemotron-1b-free] winner=linear best_epoch=15 best_test_cos=0.7373 saved → te3-small_to_nemotron-1b-free.pt  (611.8s)
21:25:09 [INFO]
─── [13/49] te3-small → fastembed-bge-small ───
21:25:09 [INFO] [te3-small_to_fastembed-bge-small] 1536d → 384d
21:25:16 [INFO] [te3-small_to_fastembed-bge-small][linear] 01/15  train_loss=0.07611  test_loss=0.11834  test_cos=0.8817  lr=1.00e-03
21:25:23 [INFO] [te3-small_to_fastembed-bge-small][linear] 02/15  train_loss=0.06962  test_loss=0.10876  test_cos=0.8912  lr=1.00e-03
21:25:30 [INFO] [te3-small_to_fastembed-bge-small][linear] 03/15  train_loss=0.06855  test_loss=0.10408  test_cos=0.8959  lr=1.00e-03
21:25:37 [INFO] [te3-small_to_fastembed-bge-small][linear] 04/15  train_loss=0.06804  test_loss=0.10058  test_cos=0.8994  lr=1.00e-03
21:25:44 [INFO] [te3-small_to_fastembed-bge-small][linear] 05/15  train_loss=0.06771  test_loss=0.09785  test_cos=0.9022  lr=1.00e-03
21:25:50 [INFO] [te3-small_to_fastembed-bge-small][linear] 06/15  train_loss=0.06748  test_loss=0.09565  test_cos=0.9044  lr=1.00e-03
21:25:57 [INFO] [te3-small_to_fastembed-bge-small][linear] 07/15  train_loss=0.06730  test_loss=0.09384  test_cos=0.9062  lr=1.00e-03
21:26:04 [INFO] [te3-small_to_fastembed-bge-small][linear] 08/15  train_loss=0.06716  test_loss=0.09234  test_cos=0.9077  lr=1.00e-03
21:26:11 [INFO] [te3-small_to_fastembed-bge-small][linear] 09/15  train_loss=0.06705  test_loss=0.09107  test_cos=0.9089  lr=1.00e-03
21:26:18 [INFO] [te3-small_to_fastembed-bge-small][linear] 10/15  train_loss=0.06697  test_loss=0.08998  test_cos=0.9100  lr=1.00e-03
21:26:25 [INFO] [te3-small_to_fastembed-bge-small][linear] 11/15  train_loss=0.06689  test_loss=0.08903  test_cos=0.9110  lr=1.00e-03
21:26:32 [INFO] [te3-small_to_fastembed-bge-small][linear] 12/15  train_loss=0.06683  test_loss=0.08820  test_cos=0.9118  lr=1.00e-03
21:26:39 [INFO] [te3-small_to_fastembed-bge-small][linear] 13/15  train_loss=0.06677  test_loss=0.08745  test_cos=0.9125  lr=1.00e-03
21:26:45 [INFO] [te3-small_to_fastembed-bge-small][linear] 14/15  train_loss=0.06672  test_loss=0.08679  test_cos=0.9132  lr=1.00e-03
21:26:52 [INFO] [te3-small_to_fastembed-bge-small][linear] 15/15  train_loss=0.06668  test_loss=0.08619  test_cos=0.9138  lr=1.00e-03
21:26:58 [INFO] [te3-small_to_fastembed-bge-small][deep] 01/15  train_loss=0.09108  test_loss=0.14030  test_cos=0.8597  lr=1.00e-03
21:27:05 [INFO] [te3-small_to_fastembed-bge-small][deep] 02/15  train_loss=0.07689  test_loss=0.12340  test_cos=0.8766  lr=1.00e-03
21:27:11 [INFO] [te3-small_to_fastembed-bge-small][deep] 03/15  train_loss=0.07549  test_loss=0.11758  test_cos=0.8824  lr=1.00e-03
21:27:17 [INFO] [te3-small_to_fastembed-bge-small][deep] 04/15  train_loss=0.07492  test_loss=0.11371  test_cos=0.8863  lr=1.00e-03
21:27:23 [INFO] [te3-small_to_fastembed-bge-small][deep] 05/15  train_loss=0.07459  test_loss=0.11117  test_cos=0.8888  lr=1.00e-03
21:27:29 [INFO] [te3-small_to_fastembed-bge-small][deep] 06/15  train_loss=0.07437  test_loss=0.10925  test_cos=0.8908  lr=1.00e-03
21:27:35 [INFO] [te3-small_to_fastembed-bge-small][deep] 07/15  train_loss=0.07421  test_loss=0.10766  test_cos=0.8923  lr=1.00e-03
21:27:41 [INFO] [te3-small_to_fastembed-bge-small][deep] 08/15  train_loss=0.07409  test_loss=0.10631  test_cos=0.8937  lr=1.00e-03
21:27:47 [INFO] [te3-small_to_fastembed-bge-small][deep] 09/15  train_loss=0.07399  test_loss=0.10514  test_cos=0.8949  lr=1.00e-03
21:27:53 [INFO] [te3-small_to_fastembed-bge-small][deep] 10/15  train_loss=0.07390  test_loss=0.10414  test_cos=0.8959  lr=1.00e-03
21:27:59 [INFO] [te3-small_to_fastembed-bge-small][deep] 11/15  train_loss=0.07383  test_loss=0.10329  test_cos=0.8967  lr=1.00e-03
21:28:05 [INFO] [te3-small_to_fastembed-bge-small][deep] 12/15  train_loss=0.07376  test_loss=0.10257  test_cos=0.8974  lr=1.00e-03
21:28:11 [INFO] [te3-small_to_fastembed-bge-small][deep] 13/15  train_loss=0.07370  test_loss=0.10196  test_cos=0.8980  lr=1.00e-03
21:28:17 [INFO] [te3-small_to_fastembed-bge-small][deep] 14/15  train_loss=0.07364  test_loss=0.10144  test_cos=0.8986  lr=1.00e-03
21:28:23 [INFO] [te3-small_to_fastembed-bge-small][deep] 15/15  train_loss=0.07359  test_loss=0.10100  test_cos=0.8990  lr=1.00e-03
21:28:23 [INFO] [te3-small_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.9138 saved → te3-small_to_fastembed-bge-small.pt  (193.9s)
21:28:23 [INFO]
─── [14/49] qwen3-emb-8b → te3-small ───
21:28:23 [INFO] [qwen3-emb-8b_to_te3-small] 4096d → 1536d
21:29:00 [INFO] [qwen3-emb-8b_to_te3-small][linear] 01/15  train_loss=0.12308  test_loss=0.17076  test_cos=0.8292  lr=1.00e-03
21:29:38 [INFO] [qwen3-emb-8b_to_te3-small][linear] 02/15  train_loss=0.10506  test_loss=0.15281  test_cos=0.8472  lr=1.00e-03
21:30:16 [INFO] [qwen3-emb-8b_to_te3-small][linear] 03/15  train_loss=0.10177  test_loss=0.14483  test_cos=0.8552  lr=1.00e-03
21:30:53 [INFO] [qwen3-emb-8b_to_te3-small][linear] 04/15  train_loss=0.09999  test_loss=0.13950  test_cos=0.8605  lr=1.00e-03
21:31:31 [INFO] [qwen3-emb-8b_to_te3-small][linear] 05/15  train_loss=0.09879  test_loss=0.13550  test_cos=0.8645  lr=1.00e-03
21:32:09 [INFO] [qwen3-emb-8b_to_te3-small][linear] 06/15  train_loss=0.09791  test_loss=0.13232  test_cos=0.8677  lr=1.00e-03
21:32:46 [INFO] [qwen3-emb-8b_to_te3-small][linear] 07/15  train_loss=0.09723  test_loss=0.12971  test_cos=0.8703  lr=1.00e-03
21:33:24 [INFO] [qwen3-emb-8b_to_te3-small][linear] 08/15  train_loss=0.09669  test_loss=0.12751  test_cos=0.8725  lr=1.00e-03
21:34:03 [INFO] [qwen3-emb-8b_to_te3-small][linear] 09/15  train_loss=0.09624  test_loss=0.12564  test_cos=0.8744  lr=1.00e-03
21:34:41 [INFO] [qwen3-emb-8b_to_te3-small][linear] 10/15  train_loss=0.09586  test_loss=0.12403  test_cos=0.8760  lr=1.00e-03
21:35:19 [INFO] [qwen3-emb-8b_to_te3-small][linear] 11/15  train_loss=0.09554  test_loss=0.12264  test_cos=0.8774  lr=1.00e-03
21:35:56 [INFO] [qwen3-emb-8b_to_te3-small][linear] 12/15  train_loss=0.09526  test_loss=0.12143  test_cos=0.8786  lr=1.00e-03
21:36:34 [INFO] [qwen3-emb-8b_to_te3-small][linear] 13/15  train_loss=0.09502  test_loss=0.12037  test_cos=0.8796  lr=1.00e-03
21:37:12 [INFO] [qwen3-emb-8b_to_te3-small][linear] 14/15  train_loss=0.09480  test_loss=0.11943  test_cos=0.8806  lr=1.00e-03
21:37:49 [INFO] [qwen3-emb-8b_to_te3-small][linear] 15/15  train_loss=0.09461  test_loss=0.11859  test_cos=0.8814  lr=1.00e-03
21:38:19 [INFO] [qwen3-emb-8b_to_te3-small][deep] 01/15  train_loss=0.14647  test_loss=0.20579  test_cos=0.7942  lr=1.00e-03
21:38:48 [INFO] [qwen3-emb-8b_to_te3-small][deep] 02/15  train_loss=0.11349  test_loss=0.17787  test_cos=0.8221  lr=1.00e-03
21:39:17 [INFO] [qwen3-emb-8b_to_te3-small][deep] 03/15  train_loss=0.10866  test_loss=0.16185  test_cos=0.8381  lr=1.00e-03
21:39:46 [INFO] [qwen3-emb-8b_to_te3-small][deep] 04/15  train_loss=0.10608  test_loss=0.15222  test_cos=0.8478  lr=1.00e-03
21:40:15 [INFO] [qwen3-emb-8b_to_te3-small][deep] 05/15  train_loss=0.10450  test_loss=0.14679  test_cos=0.8532  lr=1.00e-03
21:40:44 [INFO] [qwen3-emb-8b_to_te3-small][deep] 06/15  train_loss=0.10342  test_loss=0.14294  test_cos=0.8571  lr=1.00e-03
21:41:13 [INFO] [qwen3-emb-8b_to_te3-small][deep] 07/15  train_loss=0.10259  test_loss=0.13980  test_cos=0.8602  lr=1.00e-03
21:41:44 [INFO] [qwen3-emb-8b_to_te3-small][deep] 08/15  train_loss=0.10192  test_loss=0.13725  test_cos=0.8628  lr=1.00e-03
21:42:14 [INFO] [qwen3-emb-8b_to_te3-small][deep] 09/15  train_loss=0.10139  test_loss=0.13527  test_cos=0.8647  lr=1.00e-03
21:42:44 [INFO] [qwen3-emb-8b_to_te3-small][deep] 10/15  train_loss=0.10093  test_loss=0.13358  test_cos=0.8664  lr=1.00e-03
21:43:15 [INFO] [qwen3-emb-8b_to_te3-small][deep] 11/15  train_loss=0.10054  test_loss=0.13208  test_cos=0.8679  lr=1.00e-03
21:43:46 [INFO] [qwen3-emb-8b_to_te3-small][deep] 12/15  train_loss=0.10020  test_loss=0.13079  test_cos=0.8692  lr=1.00e-03
21:44:16 [INFO] [qwen3-emb-8b_to_te3-small][deep] 13/15  train_loss=0.09990  test_loss=0.12967  test_cos=0.8703  lr=1.00e-03
21:44:46 [INFO] [qwen3-emb-8b_to_te3-small][deep] 14/15  train_loss=0.09963  test_loss=0.12868  test_cos=0.8713  lr=1.00e-03
21:45:16 [INFO] [qwen3-emb-8b_to_te3-small][deep] 15/15  train_loss=0.09939  test_loss=0.12778  test_cos=0.8722  lr=1.00e-03
21:45:16 [INFO] [qwen3-emb-8b_to_te3-small] winner=linear best_epoch=15 best_test_cos=0.8814 saved → qwen3-emb-8b_to_te3-small.pt  (1013.0s)
21:45:16 [INFO]
─── [15/49] qwen3-emb-8b → bge-m3 ───
21:45:16 [INFO] [qwen3-emb-8b_to_bge-m3] 4096d → 1024d
21:45:44 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 01/15  train_loss=0.11913  test_loss=0.14636  test_cos=0.8536  lr=1.00e-03
21:46:12 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 02/15  train_loss=0.10549  test_loss=0.13610  test_cos=0.8639  lr=1.00e-03
21:46:40 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 03/15  train_loss=0.10282  test_loss=0.13097  test_cos=0.8690  lr=1.00e-03
21:47:08 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 04/15  train_loss=0.10132  test_loss=0.12741  test_cos=0.8726  lr=1.00e-03
21:47:35 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 05/15  train_loss=0.10031  test_loss=0.12468  test_cos=0.8753  lr=1.00e-03
21:48:03 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 06/15  train_loss=0.09956  test_loss=0.12253  test_cos=0.8775  lr=1.00e-03
21:48:31 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 07/15  train_loss=0.09897  test_loss=0.12080  test_cos=0.8792  lr=1.00e-03
21:48:59 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 08/15  train_loss=0.09850  test_loss=0.11940  test_cos=0.8806  lr=1.00e-03
21:49:27 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 09/15  train_loss=0.09811  test_loss=0.11823  test_cos=0.8818  lr=1.00e-03
21:49:55 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 10/15  train_loss=0.09779  test_loss=0.11724  test_cos=0.8828  lr=1.00e-03
21:50:23 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 11/15  train_loss=0.09751  test_loss=0.11638  test_cos=0.8836  lr=1.00e-03
21:50:50 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 12/15  train_loss=0.09727  test_loss=0.11563  test_cos=0.8844  lr=1.00e-03
21:51:18 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 13/15  train_loss=0.09705  test_loss=0.11497  test_cos=0.8850  lr=1.00e-03
21:51:46 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 14/15  train_loss=0.09687  test_loss=0.11437  test_cos=0.8856  lr=1.00e-03
21:52:13 [INFO] [qwen3-emb-8b_to_bge-m3][linear] 15/15  train_loss=0.09670  test_loss=0.11383  test_cos=0.8862  lr=1.00e-03
21:52:34 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 01/15  train_loss=0.13328  test_loss=0.16443  test_cos=0.8356  lr=1.00e-03
21:52:55 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 02/15  train_loss=0.10908  test_loss=0.14870  test_cos=0.8513  lr=1.00e-03
21:53:16 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 03/15  train_loss=0.10562  test_loss=0.14077  test_cos=0.8592  lr=1.00e-03
21:53:36 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 04/15  train_loss=0.10383  test_loss=0.13604  test_cos=0.8640  lr=1.00e-03
21:53:57 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 05/15  train_loss=0.10270  test_loss=0.13270  test_cos=0.8673  lr=1.00e-03
21:54:18 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 06/15  train_loss=0.10187  test_loss=0.13011  test_cos=0.8699  lr=1.00e-03
21:54:39 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 07/15  train_loss=0.10123  test_loss=0.12803  test_cos=0.8720  lr=1.00e-03
21:54:59 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 08/15  train_loss=0.10073  test_loss=0.12632  test_cos=0.8737  lr=1.00e-03
21:55:20 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 09/15  train_loss=0.10033  test_loss=0.12491  test_cos=0.8751  lr=1.00e-03
21:55:40 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 10/15  train_loss=0.09999  test_loss=0.12372  test_cos=0.8763  lr=1.00e-03
21:56:02 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 11/15  train_loss=0.09970  test_loss=0.12273  test_cos=0.8773  lr=1.00e-03
21:56:24 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 12/15  train_loss=0.09945  test_loss=0.12198  test_cos=0.8780  lr=1.00e-03
21:56:45 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 13/15  train_loss=0.09923  test_loss=0.12137  test_cos=0.8786  lr=1.00e-03
21:57:05 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 14/15  train_loss=0.09903  test_loss=0.12072  test_cos=0.8793  lr=1.00e-03
21:57:26 [INFO] [qwen3-emb-8b_to_bge-m3][deep] 15/15  train_loss=0.09884  test_loss=0.12006  test_cos=0.8799  lr=1.00e-03
21:57:26 [INFO] [qwen3-emb-8b_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8862 saved → qwen3-emb-8b_to_bge-m3.pt  (730.1s)
21:57:26 [INFO]
─── [16/49] qwen3-emb-8b → me5-large ───
21:57:26 [INFO] [qwen3-emb-8b_to_me5-large] 4096d → 1024d
21:57:53 [INFO] [qwen3-emb-8b_to_me5-large][linear] 01/15  train_loss=0.04685  test_loss=0.06129  test_cos=0.9387  lr=1.00e-03
21:58:20 [INFO] [qwen3-emb-8b_to_me5-large][linear] 02/15  train_loss=0.04090  test_loss=0.05667  test_cos=0.9433  lr=1.00e-03
21:58:47 [INFO] [qwen3-emb-8b_to_me5-large][linear] 03/15  train_loss=0.03978  test_loss=0.05414  test_cos=0.9459  lr=1.00e-03
21:59:14 [INFO] [qwen3-emb-8b_to_me5-large][linear] 04/15  train_loss=0.03916  test_loss=0.05233  test_cos=0.9477  lr=1.00e-03
21:59:41 [INFO] [qwen3-emb-8b_to_me5-large][linear] 05/15  train_loss=0.03873  test_loss=0.05099  test_cos=0.9490  lr=1.00e-03
22:00:08 [INFO] [qwen3-emb-8b_to_me5-large][linear] 06/15  train_loss=0.03841  test_loss=0.04999  test_cos=0.9500  lr=1.00e-03
22:00:35 [INFO] [qwen3-emb-8b_to_me5-large][linear] 07/15  train_loss=0.03817  test_loss=0.04920  test_cos=0.9508  lr=1.00e-03
22:01:02 [INFO] [qwen3-emb-8b_to_me5-large][linear] 08/15  train_loss=0.03798  test_loss=0.04857  test_cos=0.9514  lr=1.00e-03
22:01:28 [INFO] [qwen3-emb-8b_to_me5-large][linear] 09/15  train_loss=0.03782  test_loss=0.04805  test_cos=0.9520  lr=1.00e-03
22:01:55 [INFO] [qwen3-emb-8b_to_me5-large][linear] 10/15  train_loss=0.03768  test_loss=0.04761  test_cos=0.9524  lr=1.00e-03
22:02:22 [INFO] [qwen3-emb-8b_to_me5-large][linear] 11/15  train_loss=0.03757  test_loss=0.04723  test_cos=0.9528  lr=1.00e-03
22:02:49 [INFO] [qwen3-emb-8b_to_me5-large][linear] 12/15  train_loss=0.03747  test_loss=0.04690  test_cos=0.9531  lr=1.00e-03
22:03:16 [INFO] [qwen3-emb-8b_to_me5-large][linear] 13/15  train_loss=0.03738  test_loss=0.04660  test_cos=0.9534  lr=1.00e-03
22:03:42 [INFO] [qwen3-emb-8b_to_me5-large][linear] 14/15  train_loss=0.03731  test_loss=0.04634  test_cos=0.9537  lr=1.00e-03
22:04:10 [INFO] [qwen3-emb-8b_to_me5-large][linear] 15/15  train_loss=0.03724  test_loss=0.04611  test_cos=0.9539  lr=1.00e-03
22:04:30 [INFO] [qwen3-emb-8b_to_me5-large][deep] 01/15  train_loss=0.05495  test_loss=0.07094  test_cos=0.9291  lr=1.00e-03
22:04:50 [INFO] [qwen3-emb-8b_to_me5-large][deep] 02/15  train_loss=0.04268  test_loss=0.06577  test_cos=0.9342  lr=1.00e-03
22:05:10 [INFO] [qwen3-emb-8b_to_me5-large][deep] 03/15  train_loss=0.04120  test_loss=0.06222  test_cos=0.9378  lr=1.00e-03
22:05:30 [INFO] [qwen3-emb-8b_to_me5-large][deep] 04/15  train_loss=0.04041  test_loss=0.05887  test_cos=0.9411  lr=1.00e-03
22:05:50 [INFO] [qwen3-emb-8b_to_me5-large][deep] 05/15  train_loss=0.03990  test_loss=0.05698  test_cos=0.9430  lr=1.00e-03
22:06:10 [INFO] [qwen3-emb-8b_to_me5-large][deep] 06/15  train_loss=0.03956  test_loss=0.05538  test_cos=0.9446  lr=1.00e-03
22:06:30 [INFO] [qwen3-emb-8b_to_me5-large][deep] 07/15  train_loss=0.03930  test_loss=0.05411  test_cos=0.9459  lr=1.00e-03
22:06:50 [INFO] [qwen3-emb-8b_to_me5-large][deep] 08/15  train_loss=0.03909  test_loss=0.05309  test_cos=0.9469  lr=1.00e-03
22:07:10 [INFO] [qwen3-emb-8b_to_me5-large][deep] 09/15  train_loss=0.03893  test_loss=0.05230  test_cos=0.9477  lr=1.00e-03
22:07:30 [INFO] [qwen3-emb-8b_to_me5-large][deep] 10/15  train_loss=0.03880  test_loss=0.05174  test_cos=0.9483  lr=1.00e-03
22:07:50 [INFO] [qwen3-emb-8b_to_me5-large][deep] 11/15  train_loss=0.03870  test_loss=0.05139  test_cos=0.9486  lr=1.00e-03
22:08:10 [INFO] [qwen3-emb-8b_to_me5-large][deep] 12/15  train_loss=0.03861  test_loss=0.05110  test_cos=0.9489  lr=1.00e-03
22:08:30 [INFO] [qwen3-emb-8b_to_me5-large][deep] 13/15  train_loss=0.03852  test_loss=0.05079  test_cos=0.9492  lr=1.00e-03
22:08:50 [INFO] [qwen3-emb-8b_to_me5-large][deep] 14/15  train_loss=0.03843  test_loss=0.05048  test_cos=0.9495  lr=1.00e-03
22:09:10 [INFO] [qwen3-emb-8b_to_me5-large][deep] 15/15  train_loss=0.03836  test_loss=0.05019  test_cos=0.9498  lr=1.00e-03
22:09:10 [INFO] [qwen3-emb-8b_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9539 saved → qwen3-emb-8b_to_me5-large.pt  (704.2s)
22:09:10 [INFO]
─── [17/49] qwen3-emb-8b → pplx-embed-1 ───
22:09:10 [INFO] [qwen3-emb-8b_to_pplx-embed-1] 4096d → 1024d
22:09:36 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 01/15  train_loss=0.16703  test_loss=0.22565  test_cos=0.7744  lr=1.00e-03
22:10:03 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 02/15  train_loss=0.14583  test_loss=0.20439  test_cos=0.7956  lr=1.00e-03
22:10:29 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 03/15  train_loss=0.14159  test_loss=0.19439  test_cos=0.8056  lr=1.00e-03
22:10:56 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 04/15  train_loss=0.13928  test_loss=0.18761  test_cos=0.8124  lr=1.00e-03
22:11:22 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 05/15  train_loss=0.13771  test_loss=0.18247  test_cos=0.8175  lr=1.00e-03
22:11:49 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 06/15  train_loss=0.13656  test_loss=0.17837  test_cos=0.8216  lr=1.00e-03
22:12:16 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 07/15  train_loss=0.13566  test_loss=0.17506  test_cos=0.8249  lr=1.00e-03
22:12:43 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 08/15  train_loss=0.13494  test_loss=0.17232  test_cos=0.8277  lr=1.00e-03
22:13:10 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 09/15  train_loss=0.13434  test_loss=0.17003  test_cos=0.8300  lr=1.00e-03
22:13:37 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 10/15  train_loss=0.13384  test_loss=0.16806  test_cos=0.8319  lr=1.00e-03
22:14:03 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 11/15  train_loss=0.13341  test_loss=0.16634  test_cos=0.8337  lr=1.00e-03
22:14:30 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 12/15  train_loss=0.13304  test_loss=0.16484  test_cos=0.8352  lr=1.00e-03
22:14:56 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 13/15  train_loss=0.13272  test_loss=0.16351  test_cos=0.8365  lr=1.00e-03
22:15:23 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 14/15  train_loss=0.13243  test_loss=0.16233  test_cos=0.8377  lr=1.00e-03
22:15:49 [INFO] [qwen3-emb-8b_to_pplx-embed-1][linear] 15/15  train_loss=0.13217  test_loss=0.16128  test_cos=0.8387  lr=1.00e-03
22:16:09 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 01/15  train_loss=0.19681  test_loss=0.27153  test_cos=0.7285  lr=1.00e-03
22:16:29 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 02/15  train_loss=0.16048  test_loss=0.23862  test_cos=0.7614  lr=1.00e-03
22:16:49 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 03/15  train_loss=0.15560  test_loss=0.22520  test_cos=0.7748  lr=1.00e-03
22:17:09 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 04/15  train_loss=0.15317  test_loss=0.21598  test_cos=0.7840  lr=1.00e-03
22:17:29 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 05/15  train_loss=0.15169  test_loss=0.20958  test_cos=0.7904  lr=1.00e-03
22:17:49 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 06/15  train_loss=0.15065  test_loss=0.20467  test_cos=0.7953  lr=1.00e-03
22:18:09 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 07/15  train_loss=0.14986  test_loss=0.20070  test_cos=0.7993  lr=1.00e-03
22:18:30 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 08/15  train_loss=0.14924  test_loss=0.19758  test_cos=0.8024  lr=1.00e-03
22:18:50 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 09/15  train_loss=0.14873  test_loss=0.19513  test_cos=0.8049  lr=1.00e-03
22:19:10 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 10/15  train_loss=0.14831  test_loss=0.19315  test_cos=0.8069  lr=1.00e-03
22:19:30 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 11/15  train_loss=0.14795  test_loss=0.19152  test_cos=0.8085  lr=1.00e-03
22:19:51 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 12/15  train_loss=0.14764  test_loss=0.19014  test_cos=0.8099  lr=1.00e-03
22:20:12 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 13/15  train_loss=0.14737  test_loss=0.18893  test_cos=0.8111  lr=1.00e-03
22:20:33 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 14/15  train_loss=0.14713  test_loss=0.18785  test_cos=0.8122  lr=1.00e-03
22:20:54 [INFO] [qwen3-emb-8b_to_pplx-embed-1][deep] 15/15  train_loss=0.14692  test_loss=0.18689  test_cos=0.8131  lr=1.00e-03
22:20:54 [INFO] [qwen3-emb-8b_to_pplx-embed-1] winner=linear best_epoch=15 best_test_cos=0.8387 saved → qwen3-emb-8b_to_pplx-embed-1.pt  (703.9s)
22:20:54 [INFO]
─── [18/49] qwen3-emb-8b → nemotron-1b-free ───
22:20:54 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] 4096d → 2048d
22:21:44 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 01/15  train_loss=0.19781  test_loss=0.24127  test_cos=0.7587  lr=1.00e-03
22:22:34 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 02/15  train_loss=0.16914  test_loss=0.22237  test_cos=0.7776  lr=1.00e-03
22:23:23 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 03/15  train_loss=0.16451  test_loss=0.21330  test_cos=0.7867  lr=1.00e-03
22:24:12 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 04/15  train_loss=0.16198  test_loss=0.20716  test_cos=0.7928  lr=1.00e-03
22:25:01 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 05/15  train_loss=0.16027  test_loss=0.20246  test_cos=0.7975  lr=1.00e-03
22:25:50 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 06/15  train_loss=0.15901  test_loss=0.19872  test_cos=0.8013  lr=1.00e-03
22:26:38 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 07/15  train_loss=0.15803  test_loss=0.19570  test_cos=0.8043  lr=1.00e-03
22:27:28 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 08/15  train_loss=0.15724  test_loss=0.19322  test_cos=0.8068  lr=1.00e-03
22:28:18 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 09/15  train_loss=0.15660  test_loss=0.19115  test_cos=0.8089  lr=1.00e-03
22:29:04 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 10/15  train_loss=0.15605  test_loss=0.18937  test_cos=0.8106  lr=1.00e-03
22:29:50 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 11/15  train_loss=0.15558  test_loss=0.18783  test_cos=0.8122  lr=1.00e-03
22:30:35 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 12/15  train_loss=0.15518  test_loss=0.18647  test_cos=0.8135  lr=1.00e-03
22:31:21 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 13/15  train_loss=0.15483  test_loss=0.18526  test_cos=0.8147  lr=1.00e-03
22:32:06 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 14/15  train_loss=0.15451  test_loss=0.18418  test_cos=0.8158  lr=1.00e-03
22:32:52 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][linear] 15/15  train_loss=0.15423  test_loss=0.18321  test_cos=0.8168  lr=1.00e-03
22:33:30 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 01/15  train_loss=0.23244  test_loss=0.27392  test_cos=0.7261  lr=1.00e-03
22:34:07 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 02/15  train_loss=0.18040  test_loss=0.24369  test_cos=0.7563  lr=1.00e-03
22:34:45 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 03/15  train_loss=0.17339  test_loss=0.23125  test_cos=0.7687  lr=1.00e-03
22:35:22 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 04/15  train_loss=0.16977  test_loss=0.22273  test_cos=0.7773  lr=1.00e-03
22:36:00 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 05/15  train_loss=0.16754  test_loss=0.21701  test_cos=0.7830  lr=1.00e-03
22:36:37 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 06/15  train_loss=0.16603  test_loss=0.21273  test_cos=0.7873  lr=1.00e-03
22:37:14 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 07/15  train_loss=0.16491  test_loss=0.20915  test_cos=0.7909  lr=1.00e-03
22:37:51 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 08/15  train_loss=0.16402  test_loss=0.20623  test_cos=0.7938  lr=1.00e-03
22:38:29 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 09/15  train_loss=0.16330  test_loss=0.20384  test_cos=0.7962  lr=1.00e-03
22:39:06 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 10/15  train_loss=0.16271  test_loss=0.20189  test_cos=0.7981  lr=1.00e-03
22:39:44 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 11/15  train_loss=0.16221  test_loss=0.20022  test_cos=0.7998  lr=1.00e-03
22:40:21 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 12/15  train_loss=0.16178  test_loss=0.19873  test_cos=0.8013  lr=1.00e-03
22:40:58 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 13/15  train_loss=0.16141  test_loss=0.19742  test_cos=0.8026  lr=1.00e-03
22:41:35 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 14/15  train_loss=0.16109  test_loss=0.19626  test_cos=0.8037  lr=1.00e-03
22:42:12 [INFO] [qwen3-emb-8b_to_nemotron-1b-free][deep] 15/15  train_loss=0.16080  test_loss=0.19526  test_cos=0.8047  lr=1.00e-03
22:42:12 [INFO] [qwen3-emb-8b_to_nemotron-1b-free] winner=linear best_epoch=15 best_test_cos=0.8168 saved → qwen3-emb-8b_to_nemotron-1b-free.pt  (1278.2s)
22:42:12 [INFO]
─── [19/49] qwen3-emb-8b → fastembed-bge-small ───
22:42:12 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] 4096d → 384d
22:42:27 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 01/15  train_loss=0.06753  test_loss=0.09982  test_cos=0.9002  lr=1.00e-03
22:42:41 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 02/15  train_loss=0.06014  test_loss=0.08867  test_cos=0.9113  lr=1.00e-03
22:42:56 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 03/15  train_loss=0.05830  test_loss=0.08358  test_cos=0.9164  lr=1.00e-03
22:43:10 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 04/15  train_loss=0.05729  test_loss=0.08017  test_cos=0.9198  lr=1.00e-03
22:43:25 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 05/15  train_loss=0.05661  test_loss=0.07754  test_cos=0.9225  lr=1.00e-03
22:43:39 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 06/15  train_loss=0.05611  test_loss=0.07547  test_cos=0.9245  lr=1.00e-03
22:43:53 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 07/15  train_loss=0.05573  test_loss=0.07382  test_cos=0.9262  lr=1.00e-03
22:44:08 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 08/15  train_loss=0.05542  test_loss=0.07248  test_cos=0.9275  lr=1.00e-03
22:44:22 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 09/15  train_loss=0.05517  test_loss=0.07137  test_cos=0.9286  lr=1.00e-03
22:44:36 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 10/15  train_loss=0.05496  test_loss=0.07045  test_cos=0.9296  lr=1.00e-03
22:44:51 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 11/15  train_loss=0.05478  test_loss=0.06966  test_cos=0.9303  lr=1.00e-03
22:45:05 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 12/15  train_loss=0.05462  test_loss=0.06899  test_cos=0.9310  lr=1.00e-03
22:45:20 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 13/15  train_loss=0.05449  test_loss=0.06840  test_cos=0.9316  lr=1.00e-03
22:45:34 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 14/15  train_loss=0.05437  test_loss=0.06788  test_cos=0.9321  lr=1.00e-03
22:45:49 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][linear] 15/15  train_loss=0.05426  test_loss=0.06741  test_cos=0.9326  lr=1.00e-03
22:46:01 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 01/15  train_loss=0.08702  test_loss=0.12792  test_cos=0.8721  lr=1.00e-03
22:46:13 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 02/15  train_loss=0.07093  test_loss=0.10932  test_cos=0.8907  lr=1.00e-03
22:46:25 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 03/15  train_loss=0.06890  test_loss=0.10242  test_cos=0.8976  lr=1.00e-03
22:46:37 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 04/15  train_loss=0.06798  test_loss=0.09866  test_cos=0.9013  lr=1.00e-03
22:46:48 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 05/15  train_loss=0.06745  test_loss=0.09596  test_cos=0.9040  lr=1.00e-03
22:47:00 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 06/15  train_loss=0.06709  test_loss=0.09359  test_cos=0.9064  lr=1.00e-03
22:47:12 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 07/15  train_loss=0.06681  test_loss=0.09186  test_cos=0.9081  lr=1.00e-03
22:47:24 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 08/15  train_loss=0.06659  test_loss=0.09062  test_cos=0.9094  lr=1.00e-03
22:47:36 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 09/15  train_loss=0.06642  test_loss=0.08968  test_cos=0.9103  lr=1.00e-03
22:47:48 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 10/15  train_loss=0.06628  test_loss=0.08893  test_cos=0.9111  lr=1.00e-03
22:48:00 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 11/15  train_loss=0.06617  test_loss=0.08830  test_cos=0.9117  lr=1.00e-03
22:48:12 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 12/15  train_loss=0.06607  test_loss=0.08776  test_cos=0.9122  lr=1.00e-03
22:48:24 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 13/15  train_loss=0.06599  test_loss=0.08732  test_cos=0.9127  lr=1.00e-03
22:48:37 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 14/15  train_loss=0.06591  test_loss=0.08696  test_cos=0.9130  lr=1.00e-03
22:48:50 [INFO] [qwen3-emb-8b_to_fastembed-bge-small][deep] 15/15  train_loss=0.06585  test_loss=0.08669  test_cos=0.9133  lr=1.00e-03
22:48:50 [INFO] [qwen3-emb-8b_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.9326 saved → qwen3-emb-8b_to_fastembed-bge-small.pt  (398.1s)
22:48:50 [INFO]
─── [20/49] bge-m3 → te3-small ───
22:48:50 [INFO] [bge-m3_to_te3-small] 1024d → 1536d
22:49:03 [INFO] [bge-m3_to_te3-small][linear] 01/15  train_loss=0.18838  test_loss=0.28805  test_cos=0.7119  lr=1.00e-03
22:49:16 [INFO] [bge-m3_to_te3-small][linear] 02/15  train_loss=0.17646  test_loss=0.27197  test_cos=0.7280  lr=1.00e-03
22:49:29 [INFO] [bge-m3_to_te3-small][linear] 03/15  train_loss=0.17450  test_loss=0.26298  test_cos=0.7370  lr=1.00e-03
22:49:43 [INFO] [bge-m3_to_te3-small][linear] 04/15  train_loss=0.17340  test_loss=0.25650  test_cos=0.7435  lr=1.00e-03
22:49:56 [INFO] [bge-m3_to_te3-small][linear] 05/15  train_loss=0.17264  test_loss=0.25156  test_cos=0.7484  lr=1.00e-03
22:50:09 [INFO] [bge-m3_to_te3-small][linear] 06/15  train_loss=0.17206  test_loss=0.24768  test_cos=0.7523  lr=1.00e-03
22:50:22 [INFO] [bge-m3_to_te3-small][linear] 07/15  train_loss=0.17161  test_loss=0.24456  test_cos=0.7554  lr=1.00e-03
22:50:35 [INFO] [bge-m3_to_te3-small][linear] 08/15  train_loss=0.17124  test_loss=0.24198  test_cos=0.7580  lr=1.00e-03
22:50:48 [INFO] [bge-m3_to_te3-small][linear] 09/15  train_loss=0.17094  test_loss=0.23982  test_cos=0.7602  lr=1.00e-03
22:51:01 [INFO] [bge-m3_to_te3-small][linear] 10/15  train_loss=0.17068  test_loss=0.23796  test_cos=0.7620  lr=1.00e-03
22:51:14 [INFO] [bge-m3_to_te3-small][linear] 11/15  train_loss=0.17046  test_loss=0.23635  test_cos=0.7637  lr=1.00e-03
22:51:27 [INFO] [bge-m3_to_te3-small][linear] 12/15  train_loss=0.17026  test_loss=0.23492  test_cos=0.7651  lr=1.00e-03
22:51:40 [INFO] [bge-m3_to_te3-small][linear] 13/15  train_loss=0.17009  test_loss=0.23364  test_cos=0.7664  lr=1.00e-03
22:51:53 [INFO] [bge-m3_to_te3-small][linear] 14/15  train_loss=0.16994  test_loss=0.23249  test_cos=0.7675  lr=1.00e-03
22:52:06 [INFO] [bge-m3_to_te3-small][linear] 15/15  train_loss=0.16980  test_loss=0.23144  test_cos=0.7686  lr=1.00e-03
22:52:18 [INFO] [bge-m3_to_te3-small][deep] 01/15  train_loss=0.20222  test_loss=0.30390  test_cos=0.6961  lr=1.00e-03
22:52:30 [INFO] [bge-m3_to_te3-small][deep] 02/15  train_loss=0.17836  test_loss=0.28391  test_cos=0.7161  lr=1.00e-03
22:52:42 [INFO] [bge-m3_to_te3-small][deep] 03/15  train_loss=0.17504  test_loss=0.27259  test_cos=0.7274  lr=1.00e-03
22:52:54 [INFO] [bge-m3_to_te3-small][deep] 04/15  train_loss=0.17309  test_loss=0.26441  test_cos=0.7356  lr=1.00e-03
22:53:05 [INFO] [bge-m3_to_te3-small][deep] 05/15  train_loss=0.17151  test_loss=0.25784  test_cos=0.7422  lr=1.00e-03
22:53:17 [INFO] [bge-m3_to_te3-small][deep] 06/15  train_loss=0.17010  test_loss=0.25260  test_cos=0.7474  lr=1.00e-03
22:53:29 [INFO] [bge-m3_to_te3-small][deep] 07/15  train_loss=0.16880  test_loss=0.24779  test_cos=0.7522  lr=1.00e-03
22:53:41 [INFO] [bge-m3_to_te3-small][deep] 08/15  train_loss=0.16758  test_loss=0.24343  test_cos=0.7566  lr=1.00e-03
22:53:53 [INFO] [bge-m3_to_te3-small][deep] 09/15  train_loss=0.16643  test_loss=0.23961  test_cos=0.7604  lr=1.00e-03
22:54:05 [INFO] [bge-m3_to_te3-small][deep] 10/15  train_loss=0.16537  test_loss=0.23581  test_cos=0.7642  lr=1.00e-03
22:54:18 [INFO] [bge-m3_to_te3-small][deep] 11/15  train_loss=0.16438  test_loss=0.23225  test_cos=0.7677  lr=1.00e-03
22:54:30 [INFO] [bge-m3_to_te3-small][deep] 12/15  train_loss=0.16346  test_loss=0.22885  test_cos=0.7711  lr=1.00e-03
22:54:43 [INFO] [bge-m3_to_te3-small][deep] 13/15  train_loss=0.16258  test_loss=0.22570  test_cos=0.7743  lr=1.00e-03
22:54:55 [INFO] [bge-m3_to_te3-small][deep] 14/15  train_loss=0.16176  test_loss=0.22263  test_cos=0.7774  lr=1.00e-03
22:55:07 [INFO] [bge-m3_to_te3-small][deep] 15/15  train_loss=0.16098  test_loss=0.21977  test_cos=0.7802  lr=1.00e-03
22:55:07 [INFO] [bge-m3_to_te3-small] winner=deep best_epoch=15 best_test_cos=0.7802 saved → bge-m3_to_te3-small.pt  (376.8s)
22:55:07 [INFO]
─── [21/49] bge-m3 → qwen3-emb-8b ───
22:55:07 [INFO] [bge-m3_to_qwen3-emb-8b] 1024d → 4096d
22:55:40 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 01/15  train_loss=0.21921  test_loss=0.34309  test_cos=0.6569  lr=1.00e-03
22:56:19 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 02/15  train_loss=0.20773  test_loss=0.32443  test_cos=0.6756  lr=1.00e-03
22:57:01 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 03/15  train_loss=0.20555  test_loss=0.31412  test_cos=0.6859  lr=1.00e-03
22:57:37 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 04/15  train_loss=0.20431  test_loss=0.30669  test_cos=0.6933  lr=1.00e-03
22:58:11 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 05/15  train_loss=0.20343  test_loss=0.30094  test_cos=0.6991  lr=1.00e-03
22:58:44 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 06/15  train_loss=0.20277  test_loss=0.29631  test_cos=0.7037  lr=1.00e-03
22:59:18 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 07/15  train_loss=0.20223  test_loss=0.29248  test_cos=0.7075  lr=1.00e-03
22:59:49 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 08/15  train_loss=0.20179  test_loss=0.28926  test_cos=0.7107  lr=1.00e-03
23:00:21 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 09/15  train_loss=0.20143  test_loss=0.28648  test_cos=0.7135  lr=1.00e-03
23:00:52 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 10/15  train_loss=0.20111  test_loss=0.28407  test_cos=0.7159  lr=1.00e-03
23:01:23 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 11/15  train_loss=0.20084  test_loss=0.28194  test_cos=0.7181  lr=1.00e-03
23:01:55 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 12/15  train_loss=0.20060  test_loss=0.28004  test_cos=0.7200  lr=1.00e-03
23:02:26 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 13/15  train_loss=0.20040  test_loss=0.27833  test_cos=0.7217  lr=1.00e-03
23:02:57 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 14/15  train_loss=0.20021  test_loss=0.27678  test_cos=0.7232  lr=1.00e-03
23:03:29 [INFO] [bge-m3_to_qwen3-emb-8b][linear] 15/15  train_loss=0.20005  test_loss=0.27536  test_cos=0.7246  lr=1.00e-03
23:03:54 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 01/15  train_loss=0.23652  test_loss=0.35786  test_cos=0.6421  lr=1.00e-03
23:04:19 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 02/15  train_loss=0.20904  test_loss=0.33233  test_cos=0.6677  lr=1.00e-03
23:04:44 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 03/15  train_loss=0.20462  test_loss=0.32084  test_cos=0.6792  lr=1.00e-03
23:05:11 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 04/15  train_loss=0.20164  test_loss=0.31143  test_cos=0.6886  lr=1.00e-03
23:05:36 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 05/15  train_loss=0.19926  test_loss=0.30302  test_cos=0.6970  lr=1.00e-03
23:06:01 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 06/15  train_loss=0.19717  test_loss=0.29606  test_cos=0.7039  lr=1.00e-03
23:06:26 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 07/15  train_loss=0.19532  test_loss=0.29013  test_cos=0.7099  lr=1.00e-03
23:06:51 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 08/15  train_loss=0.19365  test_loss=0.28441  test_cos=0.7156  lr=1.00e-03
23:07:17 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 09/15  train_loss=0.19219  test_loss=0.27924  test_cos=0.7208  lr=1.00e-03
23:07:43 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 10/15  train_loss=0.19090  test_loss=0.27441  test_cos=0.7256  lr=1.00e-03
23:08:08 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 11/15  train_loss=0.18976  test_loss=0.26993  test_cos=0.7301  lr=1.00e-03
23:08:33 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 12/15  train_loss=0.18873  test_loss=0.26574  test_cos=0.7343  lr=1.00e-03
23:08:59 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 13/15  train_loss=0.18779  test_loss=0.26186  test_cos=0.7381  lr=1.00e-03
23:09:25 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 14/15  train_loss=0.18690  test_loss=0.25831  test_cos=0.7417  lr=1.00e-03
23:09:50 [INFO] [bge-m3_to_qwen3-emb-8b][deep] 15/15  train_loss=0.18607  test_loss=0.25508  test_cos=0.7449  lr=1.00e-03
23:09:50 [INFO] [bge-m3_to_qwen3-emb-8b] winner=deep best_epoch=15 best_test_cos=0.7449 saved → bge-m3_to_qwen3-emb-8b.pt  (882.8s)
23:09:50 [INFO]
─── [22/49] bge-m3 → me5-large ───
23:09:50 [INFO] [bge-m3_to_me5-large] 1024d → 1024d
23:10:00 [INFO] [bge-m3_to_me5-large][linear] 01/15  train_loss=0.04743  test_loss=0.06487  test_cos=0.9351  lr=1.00e-03
23:10:11 [INFO] [bge-m3_to_me5-large][linear] 02/15  train_loss=0.04068  test_loss=0.06156  test_cos=0.9384  lr=1.00e-03
23:10:21 [INFO] [bge-m3_to_me5-large][linear] 03/15  train_loss=0.04012  test_loss=0.05982  test_cos=0.9402  lr=1.00e-03
23:10:31 [INFO] [bge-m3_to_me5-large][linear] 04/15  train_loss=0.03983  test_loss=0.05875  test_cos=0.9413  lr=1.00e-03
23:10:41 [INFO] [bge-m3_to_me5-large][linear] 05/15  train_loss=0.03964  test_loss=0.05804  test_cos=0.9420  lr=1.00e-03
23:10:52 [INFO] [bge-m3_to_me5-large][linear] 06/15  train_loss=0.03950  test_loss=0.05750  test_cos=0.9425  lr=1.00e-03
23:11:02 [INFO] [bge-m3_to_me5-large][linear] 07/15  train_loss=0.03940  test_loss=0.05705  test_cos=0.9429  lr=1.00e-03
23:11:12 [INFO] [bge-m3_to_me5-large][linear] 08/15  train_loss=0.03931  test_loss=0.05664  test_cos=0.9434  lr=1.00e-03
23:11:22 [INFO] [bge-m3_to_me5-large][linear] 09/15  train_loss=0.03925  test_loss=0.05624  test_cos=0.9438  lr=1.00e-03
23:11:32 [INFO] [bge-m3_to_me5-large][linear] 10/15  train_loss=0.03919  test_loss=0.05585  test_cos=0.9442  lr=1.00e-03
23:11:43 [INFO] [bge-m3_to_me5-large][linear] 11/15  train_loss=0.03914  test_loss=0.05547  test_cos=0.9445  lr=1.00e-03
23:11:53 [INFO] [bge-m3_to_me5-large][linear] 12/15  train_loss=0.03910  test_loss=0.05510  test_cos=0.9449  lr=1.00e-03
23:12:03 [INFO] [bge-m3_to_me5-large][linear] 13/15  train_loss=0.03907  test_loss=0.05475  test_cos=0.9453  lr=1.00e-03
23:12:13 [INFO] [bge-m3_to_me5-large][linear] 14/15  train_loss=0.03904  test_loss=0.05441  test_cos=0.9456  lr=1.00e-03
23:12:23 [INFO] [bge-m3_to_me5-large][linear] 15/15  train_loss=0.03901  test_loss=0.05409  test_cos=0.9459  lr=1.00e-03
23:12:34 [INFO] [bge-m3_to_me5-large][deep] 01/15  train_loss=0.05288  test_loss=0.07057  test_cos=0.9294  lr=1.00e-03
23:12:44 [INFO] [bge-m3_to_me5-large][deep] 02/15  train_loss=0.04153  test_loss=0.06565  test_cos=0.9343  lr=1.00e-03
23:12:54 [INFO] [bge-m3_to_me5-large][deep] 03/15  train_loss=0.04070  test_loss=0.06360  test_cos=0.9364  lr=1.00e-03
23:13:05 [INFO] [bge-m3_to_me5-large][deep] 04/15  train_loss=0.04029  test_loss=0.06196  test_cos=0.9380  lr=1.00e-03
23:13:15 [INFO] [bge-m3_to_me5-large][deep] 05/15  train_loss=0.04003  test_loss=0.06078  test_cos=0.9392  lr=1.00e-03
23:13:25 [INFO] [bge-m3_to_me5-large][deep] 06/15  train_loss=0.03993  test_loss=0.05971  test_cos=0.9403  lr=1.00e-03
23:13:36 [INFO] [bge-m3_to_me5-large][deep] 07/15  train_loss=0.03969  test_loss=0.05878  test_cos=0.9412  lr=1.00e-03
23:13:46 [INFO] [bge-m3_to_me5-large][deep] 08/15  train_loss=0.03956  test_loss=0.05790  test_cos=0.9421  lr=1.00e-03
23:13:56 [INFO] [bge-m3_to_me5-large][deep] 09/15  train_loss=0.03946  test_loss=0.05732  test_cos=0.9427  lr=1.00e-03
23:14:07 [INFO] [bge-m3_to_me5-large][deep] 10/15  train_loss=0.03937  test_loss=0.05674  test_cos=0.9433  lr=1.00e-03
23:14:17 [INFO] [bge-m3_to_me5-large][deep] 11/15  train_loss=0.03930  test_loss=0.05631  test_cos=0.9437  lr=1.00e-03
23:14:27 [INFO] [bge-m3_to_me5-large][deep] 12/15  train_loss=0.03923  test_loss=0.05588  test_cos=0.9441  lr=1.00e-03
23:14:37 [INFO] [bge-m3_to_me5-large][deep] 13/15  train_loss=0.03917  test_loss=0.05549  test_cos=0.9445  lr=1.00e-03
23:14:48 [INFO] [bge-m3_to_me5-large][deep] 14/15  train_loss=0.03912  test_loss=0.05512  test_cos=0.9449  lr=1.00e-03
23:14:58 [INFO] [bge-m3_to_me5-large][deep] 15/15  train_loss=0.03906  test_loss=0.05479  test_cos=0.9452  lr=1.00e-03
23:14:58 [INFO] [bge-m3_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9459 saved → bge-m3_to_me5-large.pt  (307.9s)
23:14:58 [INFO]
─── [23/49] bge-m3 → pplx-embed-1 ───
23:14:58 [INFO] [bge-m3_to_pplx-embed-1] 1024d → 1024d
23:15:08 [INFO] [bge-m3_to_pplx-embed-1][linear] 01/15  train_loss=0.25866  test_loss=0.37903  test_cos=0.6210  lr=1.00e-03
23:15:18 [INFO] [bge-m3_to_pplx-embed-1][linear] 02/15  train_loss=0.24598  test_loss=0.35877  test_cos=0.6412  lr=1.00e-03
23:15:28 [INFO] [bge-m3_to_pplx-embed-1][linear] 03/15  train_loss=0.24330  test_loss=0.34726  test_cos=0.6527  lr=1.00e-03
23:15:45 [INFO] [bge-m3_to_pplx-embed-1][linear] 04/15  train_loss=0.24176  test_loss=0.33891  test_cos=0.6611  lr=1.00e-03
23:15:57 [INFO] [bge-m3_to_pplx-embed-1][linear] 05/15  train_loss=0.24068  test_loss=0.33250  test_cos=0.6675  lr=1.00e-03
23:16:09 [INFO] [bge-m3_to_pplx-embed-1][linear] 06/15  train_loss=0.23987  test_loss=0.32744  test_cos=0.6726  lr=1.00e-03
23:16:26 [INFO] [bge-m3_to_pplx-embed-1][linear] 07/15  train_loss=0.23924  test_loss=0.32334  test_cos=0.6767  lr=1.00e-03
23:16:41 [INFO] [bge-m3_to_pplx-embed-1][linear] 08/15  train_loss=0.23872  test_loss=0.31995  test_cos=0.6801  lr=1.00e-03
23:16:57 [INFO] [bge-m3_to_pplx-embed-1][linear] 09/15  train_loss=0.23829  test_loss=0.31709  test_cos=0.6829  lr=1.00e-03
23:17:11 [INFO] [bge-m3_to_pplx-embed-1][linear] 10/15  train_loss=0.23792  test_loss=0.31463  test_cos=0.6854  lr=1.00e-03
23:17:24 [INFO] [bge-m3_to_pplx-embed-1][linear] 11/15  train_loss=0.23761  test_loss=0.31250  test_cos=0.6875  lr=1.00e-03
23:17:37 [INFO] [bge-m3_to_pplx-embed-1][linear] 12/15  train_loss=0.23734  test_loss=0.31062  test_cos=0.6894  lr=1.00e-03
23:17:47 [INFO] [bge-m3_to_pplx-embed-1][linear] 13/15  train_loss=0.23711  test_loss=0.30895  test_cos=0.6910  lr=1.00e-03
23:17:58 [INFO] [bge-m3_to_pplx-embed-1][linear] 14/15  train_loss=0.23690  test_loss=0.30745  test_cos=0.6925  lr=1.00e-03
23:18:10 [INFO] [bge-m3_to_pplx-embed-1][linear] 15/15  train_loss=0.23671  test_loss=0.30609  test_cos=0.6939  lr=1.00e-03
23:18:20 [INFO] [bge-m3_to_pplx-embed-1][deep] 01/15  train_loss=0.27114  test_loss=0.39642  test_cos=0.6036  lr=1.00e-03
23:18:31 [INFO] [bge-m3_to_pplx-embed-1][deep] 02/15  train_loss=0.24671  test_loss=0.37200  test_cos=0.6280  lr=1.00e-03
23:18:41 [INFO] [bge-m3_to_pplx-embed-1][deep] 03/15  train_loss=0.24270  test_loss=0.35852  test_cos=0.6415  lr=1.00e-03
23:18:51 [INFO] [bge-m3_to_pplx-embed-1][deep] 04/15  train_loss=0.24016  test_loss=0.34963  test_cos=0.6504  lr=1.00e-03
23:19:02 [INFO] [bge-m3_to_pplx-embed-1][deep] 05/15  train_loss=0.23810  test_loss=0.34264  test_cos=0.6574  lr=1.00e-03
23:19:12 [INFO] [bge-m3_to_pplx-embed-1][deep] 06/15  train_loss=0.23624  test_loss=0.33675  test_cos=0.6632  lr=1.00e-03
23:19:22 [INFO] [bge-m3_to_pplx-embed-1][deep] 07/15  train_loss=0.23449  test_loss=0.33126  test_cos=0.6687  lr=1.00e-03
23:19:32 [INFO] [bge-m3_to_pplx-embed-1][deep] 08/15  train_loss=0.23275  test_loss=0.32564  test_cos=0.6744  lr=1.00e-03
23:19:43 [INFO] [bge-m3_to_pplx-embed-1][deep] 09/15  train_loss=0.23104  test_loss=0.31996  test_cos=0.6800  lr=1.00e-03
23:19:53 [INFO] [bge-m3_to_pplx-embed-1][deep] 10/15  train_loss=0.22938  test_loss=0.31442  test_cos=0.6856  lr=1.00e-03
23:20:03 [INFO] [bge-m3_to_pplx-embed-1][deep] 11/15  train_loss=0.22781  test_loss=0.30918  test_cos=0.6908  lr=1.00e-03
23:20:13 [INFO] [bge-m3_to_pplx-embed-1][deep] 12/15  train_loss=0.22635  test_loss=0.30431  test_cos=0.6957  lr=1.00e-03
23:20:24 [INFO] [bge-m3_to_pplx-embed-1][deep] 13/15  train_loss=0.22499  test_loss=0.29984  test_cos=0.7002  lr=1.00e-03
23:20:34 [INFO] [bge-m3_to_pplx-embed-1][deep] 14/15  train_loss=0.22372  test_loss=0.29572  test_cos=0.7043  lr=1.00e-03
23:20:44 [INFO] [bge-m3_to_pplx-embed-1][deep] 15/15  train_loss=0.22253  test_loss=0.29194  test_cos=0.7081  lr=1.00e-03
23:20:44 [INFO] [bge-m3_to_pplx-embed-1] winner=deep best_epoch=15 best_test_cos=0.7081 saved → bge-m3_to_pplx-embed-1.pt  (345.6s)
23:20:44 [INFO]
─── [24/49] bge-m3 → nemotron-1b-free ───
23:20:44 [INFO] [bge-m3_to_nemotron-1b-free] 1024d → 2048d
23:21:01 [INFO] [bge-m3_to_nemotron-1b-free][linear] 01/15  train_loss=0.32004  test_loss=0.43493  test_cos=0.5651  lr=1.00e-03
23:21:18 [INFO] [bge-m3_to_nemotron-1b-free][linear] 02/15  train_loss=0.30225  test_loss=0.41558  test_cos=0.5844  lr=1.00e-03
23:21:35 [INFO] [bge-m3_to_nemotron-1b-free][linear] 03/15  train_loss=0.29884  test_loss=0.40466  test_cos=0.5953  lr=1.00e-03
23:21:55 [INFO] [bge-m3_to_nemotron-1b-free][linear] 04/15  train_loss=0.29687  test_loss=0.39692  test_cos=0.6031  lr=1.00e-03
23:22:12 [INFO] [bge-m3_to_nemotron-1b-free][linear] 05/15  train_loss=0.29552  test_loss=0.39107  test_cos=0.6089  lr=1.00e-03
23:22:29 [INFO] [bge-m3_to_nemotron-1b-free][linear] 06/15  train_loss=0.29452  test_loss=0.38647  test_cos=0.6135  lr=1.00e-03
23:22:45 [INFO] [bge-m3_to_nemotron-1b-free][linear] 07/15  train_loss=0.29373  test_loss=0.38277  test_cos=0.6172  lr=1.00e-03
23:23:01 [INFO] [bge-m3_to_nemotron-1b-free][linear] 08/15  train_loss=0.29310  test_loss=0.37972  test_cos=0.6203  lr=1.00e-03
23:23:17 [INFO] [bge-m3_to_nemotron-1b-free][linear] 09/15  train_loss=0.29258  test_loss=0.37714  test_cos=0.6229  lr=1.00e-03
23:23:33 [INFO] [bge-m3_to_nemotron-1b-free][linear] 10/15  train_loss=0.29214  test_loss=0.37493  test_cos=0.6251  lr=1.00e-03
23:23:49 [INFO] [bge-m3_to_nemotron-1b-free][linear] 11/15  train_loss=0.29177  test_loss=0.37301  test_cos=0.6270  lr=1.00e-03
23:24:04 [INFO] [bge-m3_to_nemotron-1b-free][linear] 12/15  train_loss=0.29144  test_loss=0.37131  test_cos=0.6287  lr=1.00e-03
23:24:20 [INFO] [bge-m3_to_nemotron-1b-free][linear] 13/15  train_loss=0.29116  test_loss=0.36979  test_cos=0.6302  lr=1.00e-03
23:24:36 [INFO] [bge-m3_to_nemotron-1b-free][linear] 14/15  train_loss=0.29091  test_loss=0.36842  test_cos=0.6316  lr=1.00e-03
23:24:52 [INFO] [bge-m3_to_nemotron-1b-free][linear] 15/15  train_loss=0.29068  test_loss=0.36718  test_cos=0.6328  lr=1.00e-03
23:25:06 [INFO] [bge-m3_to_nemotron-1b-free][deep] 01/15  train_loss=0.33961  test_loss=0.45159  test_cos=0.5484  lr=1.00e-03
23:25:20 [INFO] [bge-m3_to_nemotron-1b-free][deep] 02/15  train_loss=0.30637  test_loss=0.42810  test_cos=0.5719  lr=1.00e-03
23:25:34 [INFO] [bge-m3_to_nemotron-1b-free][deep] 03/15  train_loss=0.30149  test_loss=0.41650  test_cos=0.5835  lr=1.00e-03
23:25:49 [INFO] [bge-m3_to_nemotron-1b-free][deep] 04/15  train_loss=0.29886  test_loss=0.40845  test_cos=0.5915  lr=1.00e-03
23:26:03 [INFO] [bge-m3_to_nemotron-1b-free][deep] 05/15  train_loss=0.29707  test_loss=0.40121  test_cos=0.5988  lr=1.00e-03
23:26:17 [INFO] [bge-m3_to_nemotron-1b-free][deep] 06/15  train_loss=0.29573  test_loss=0.39554  test_cos=0.6045  lr=1.00e-03
23:26:31 [INFO] [bge-m3_to_nemotron-1b-free][deep] 07/15  train_loss=0.29466  test_loss=0.38952  test_cos=0.6105  lr=1.00e-03
23:26:45 [INFO] [bge-m3_to_nemotron-1b-free][deep] 08/15  train_loss=0.29375  test_loss=0.38547  test_cos=0.6145  lr=1.00e-03
23:26:59 [INFO] [bge-m3_to_nemotron-1b-free][deep] 09/15  train_loss=0.29295  test_loss=0.38124  test_cos=0.6188  lr=1.00e-03
23:27:13 [INFO] [bge-m3_to_nemotron-1b-free][deep] 10/15  train_loss=0.29222  test_loss=0.37810  test_cos=0.6219  lr=1.00e-03
23:27:27 [INFO] [bge-m3_to_nemotron-1b-free][deep] 11/15  train_loss=0.29154  test_loss=0.37491  test_cos=0.6251  lr=1.00e-03
23:27:41 [INFO] [bge-m3_to_nemotron-1b-free][deep] 12/15  train_loss=0.29090  test_loss=0.37203  test_cos=0.6280  lr=1.00e-03
23:27:55 [INFO] [bge-m3_to_nemotron-1b-free][deep] 13/15  train_loss=0.29030  test_loss=0.36939  test_cos=0.6306  lr=1.00e-03
23:28:09 [INFO] [bge-m3_to_nemotron-1b-free][deep] 14/15  train_loss=0.28972  test_loss=0.36696  test_cos=0.6330  lr=1.00e-03
23:28:23 [INFO] [bge-m3_to_nemotron-1b-free][deep] 15/15  train_loss=0.28917  test_loss=0.36472  test_cos=0.6353  lr=1.00e-03
23:28:23 [INFO] [bge-m3_to_nemotron-1b-free] winner=deep best_epoch=15 best_test_cos=0.6353 saved → bge-m3_to_nemotron-1b-free.pt  (459.8s)
23:28:23 [INFO]
─── [25/49] bge-m3 → fastembed-bge-small ───
23:28:23 [INFO] [bge-m3_to_fastembed-bge-small] 1024d → 384d
23:28:29 [INFO] [bge-m3_to_fastembed-bge-small][linear] 01/15  train_loss=0.09316  test_loss=0.15655  test_cos=0.8435  lr=1.00e-03
23:28:34 [INFO] [bge-m3_to_fastembed-bge-small][linear] 02/15  train_loss=0.08765  test_loss=0.14853  test_cos=0.8515  lr=1.00e-03
23:28:40 [INFO] [bge-m3_to_fastembed-bge-small][linear] 03/15  train_loss=0.08683  test_loss=0.14368  test_cos=0.8563  lr=1.00e-03
23:28:45 [INFO] [bge-m3_to_fastembed-bge-small][linear] 04/15  train_loss=0.08637  test_loss=0.13978  test_cos=0.8602  lr=1.00e-03
23:28:51 [INFO] [bge-m3_to_fastembed-bge-small][linear] 05/15  train_loss=0.08605  test_loss=0.13657  test_cos=0.8634  lr=1.00e-03
23:28:56 [INFO] [bge-m3_to_fastembed-bge-small][linear] 06/15  train_loss=0.08580  test_loss=0.13393  test_cos=0.8661  lr=1.00e-03
23:29:02 [INFO] [bge-m3_to_fastembed-bge-small][linear] 07/15  train_loss=0.08559  test_loss=0.13175  test_cos=0.8683  lr=1.00e-03
23:29:08 [INFO] [bge-m3_to_fastembed-bge-small][linear] 08/15  train_loss=0.08543  test_loss=0.12992  test_cos=0.8701  lr=1.00e-03
23:29:13 [INFO] [bge-m3_to_fastembed-bge-small][linear] 09/15  train_loss=0.08529  test_loss=0.12836  test_cos=0.8716  lr=1.00e-03
23:29:19 [INFO] [bge-m3_to_fastembed-bge-small][linear] 10/15  train_loss=0.08517  test_loss=0.12702  test_cos=0.8730  lr=1.00e-03
23:29:25 [INFO] [bge-m3_to_fastembed-bge-small][linear] 11/15  train_loss=0.08507  test_loss=0.12585  test_cos=0.8741  lr=1.00e-03
23:29:30 [INFO] [bge-m3_to_fastembed-bge-small][linear] 12/15  train_loss=0.08498  test_loss=0.12482  test_cos=0.8752  lr=1.00e-03
23:29:36 [INFO] [bge-m3_to_fastembed-bge-small][linear] 13/15  train_loss=0.08491  test_loss=0.12391  test_cos=0.8761  lr=1.00e-03
23:29:41 [INFO] [bge-m3_to_fastembed-bge-small][linear] 14/15  train_loss=0.08484  test_loss=0.12308  test_cos=0.8769  lr=1.00e-03
23:29:47 [INFO] [bge-m3_to_fastembed-bge-small][linear] 15/15  train_loss=0.08478  test_loss=0.12233  test_cos=0.8777  lr=1.00e-03
23:29:52 [INFO] [bge-m3_to_fastembed-bge-small][deep] 01/15  train_loss=0.10536  test_loss=0.16983  test_cos=0.8302  lr=1.00e-03
23:29:57 [INFO] [bge-m3_to_fastembed-bge-small][deep] 02/15  train_loss=0.09140  test_loss=0.15407  test_cos=0.8459  lr=1.00e-03
23:30:02 [INFO] [bge-m3_to_fastembed-bge-small][deep] 03/15  train_loss=0.08987  test_loss=0.14796  test_cos=0.8520  lr=1.00e-03
23:30:08 [INFO] [bge-m3_to_fastembed-bge-small][deep] 04/15  train_loss=0.08912  test_loss=0.14376  test_cos=0.8562  lr=1.00e-03
23:30:13 [INFO] [bge-m3_to_fastembed-bge-small][deep] 05/15  train_loss=0.08862  test_loss=0.14058  test_cos=0.8594  lr=1.00e-03
23:30:18 [INFO] [bge-m3_to_fastembed-bge-small][deep] 06/15  train_loss=0.08824  test_loss=0.13811  test_cos=0.8619  lr=1.00e-03
23:30:23 [INFO] [bge-m3_to_fastembed-bge-small][deep] 07/15  train_loss=0.08791  test_loss=0.13601  test_cos=0.8640  lr=1.00e-03
23:30:28 [INFO] [bge-m3_to_fastembed-bge-small][deep] 08/15  train_loss=0.08763  test_loss=0.13418  test_cos=0.8658  lr=1.00e-03
23:30:34 [INFO] [bge-m3_to_fastembed-bge-small][deep] 09/15  train_loss=0.08737  test_loss=0.13259  test_cos=0.8674  lr=1.00e-03
23:30:39 [INFO] [bge-m3_to_fastembed-bge-small][deep] 10/15  train_loss=0.08713  test_loss=0.13119  test_cos=0.8688  lr=1.00e-03
23:30:44 [INFO] [bge-m3_to_fastembed-bge-small][deep] 11/15  train_loss=0.08691  test_loss=0.12991  test_cos=0.8701  lr=1.00e-03
23:30:49 [INFO] [bge-m3_to_fastembed-bge-small][deep] 12/15  train_loss=0.08671  test_loss=0.12871  test_cos=0.8713  lr=1.00e-03
23:30:54 [INFO] [bge-m3_to_fastembed-bge-small][deep] 13/15  train_loss=0.08653  test_loss=0.12758  test_cos=0.8724  lr=1.00e-03
23:31:00 [INFO] [bge-m3_to_fastembed-bge-small][deep] 14/15  train_loss=0.08636  test_loss=0.12651  test_cos=0.8735  lr=1.00e-03
23:31:05 [INFO] [bge-m3_to_fastembed-bge-small][deep] 15/15  train_loss=0.08620  test_loss=0.12550  test_cos=0.8745  lr=1.00e-03
23:31:05 [INFO] [bge-m3_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.8777 saved → bge-m3_to_fastembed-bge-small.pt  (161.3s)
23:31:05 [INFO]
─── [26/49] me5-large → te3-small ───
23:31:05 [INFO] [me5-large_to_te3-small] 1024d → 1536d
23:31:18 [INFO] [me5-large_to_te3-small][linear] 01/15  train_loss=0.19847  test_loss=0.28892  test_cos=0.7111  lr=1.00e-03
23:31:30 [INFO] [me5-large_to_te3-small][linear] 02/15  train_loss=0.17382  test_loss=0.26800  test_cos=0.7320  lr=1.00e-03
23:31:43 [INFO] [me5-large_to_te3-small][linear] 03/15  train_loss=0.17114  test_loss=0.25535  test_cos=0.7446  lr=1.00e-03
23:31:55 [INFO] [me5-large_to_te3-small][linear] 04/15  train_loss=0.16965  test_loss=0.24616  test_cos=0.7538  lr=1.00e-03
23:32:08 [INFO] [me5-large_to_te3-small][linear] 05/15  train_loss=0.16861  test_loss=0.23943  test_cos=0.7606  lr=1.00e-03
23:32:21 [INFO] [me5-large_to_te3-small][linear] 06/15  train_loss=0.16782  test_loss=0.23454  test_cos=0.7655  lr=1.00e-03
23:32:33 [INFO] [me5-large_to_te3-small][linear] 07/15  train_loss=0.16719  test_loss=0.23102  test_cos=0.7690  lr=1.00e-03
23:32:45 [INFO] [me5-large_to_te3-small][linear] 08/15  train_loss=0.16666  test_loss=0.22848  test_cos=0.7715  lr=1.00e-03
23:32:58 [INFO] [me5-large_to_te3-small][linear] 09/15  train_loss=0.16622  test_loss=0.22663  test_cos=0.7734  lr=1.00e-03
23:33:10 [INFO] [me5-large_to_te3-small][linear] 10/15  train_loss=0.16583  test_loss=0.22527  test_cos=0.7747  lr=1.00e-03
23:33:22 [INFO] [me5-large_to_te3-small][linear] 11/15  train_loss=0.16549  test_loss=0.22424  test_cos=0.7758  lr=1.00e-03
23:33:34 [INFO] [me5-large_to_te3-small][linear] 12/15  train_loss=0.16519  test_loss=0.22344  test_cos=0.7766  lr=1.00e-03
23:33:46 [INFO] [me5-large_to_te3-small][linear] 13/15  train_loss=0.16492  test_loss=0.22281  test_cos=0.7772  lr=1.00e-03
23:33:58 [INFO] [me5-large_to_te3-small][linear] 14/15  train_loss=0.16467  test_loss=0.22228  test_cos=0.7777  lr=1.00e-03
23:34:11 [INFO] [me5-large_to_te3-small][linear] 15/15  train_loss=0.16445  test_loss=0.22181  test_cos=0.7782  lr=1.00e-03
23:34:22 [INFO] [me5-large_to_te3-small][deep] 01/15  train_loss=0.21743  test_loss=0.28807  test_cos=0.7119  lr=1.00e-03
23:34:33 [INFO] [me5-large_to_te3-small][deep] 02/15  train_loss=0.17475  test_loss=0.26592  test_cos=0.7341  lr=1.00e-03
23:34:44 [INFO] [me5-large_to_te3-small][deep] 03/15  train_loss=0.17087  test_loss=0.25675  test_cos=0.7433  lr=1.00e-03
23:34:56 [INFO] [me5-large_to_te3-small][deep] 04/15  train_loss=0.16897  test_loss=0.25126  test_cos=0.7487  lr=1.00e-03
23:35:07 [INFO] [me5-large_to_te3-small][deep] 05/15  train_loss=0.16783  test_loss=0.24785  test_cos=0.7522  lr=1.00e-03
23:35:18 [INFO] [me5-large_to_te3-small][deep] 06/15  train_loss=0.16693  test_loss=0.24514  test_cos=0.7549  lr=1.00e-03
23:35:29 [INFO] [me5-large_to_te3-small][deep] 07/15  train_loss=0.16615  test_loss=0.24107  test_cos=0.7589  lr=1.00e-03
23:35:41 [INFO] [me5-large_to_te3-small][deep] 08/15  train_loss=0.16548  test_loss=0.23821  test_cos=0.7618  lr=1.00e-03
23:35:52 [INFO] [me5-large_to_te3-small][deep] 09/15  train_loss=0.16488  test_loss=0.23561  test_cos=0.7644  lr=1.00e-03
23:36:03 [INFO] [me5-large_to_te3-small][deep] 10/15  train_loss=0.16434  test_loss=0.23364  test_cos=0.7664  lr=1.00e-03
23:36:14 [INFO] [me5-large_to_te3-small][deep] 11/15  train_loss=0.16386  test_loss=0.23134  test_cos=0.7687  lr=1.00e-03
23:36:25 [INFO] [me5-large_to_te3-small][deep] 12/15  train_loss=0.16339  test_loss=0.22871  test_cos=0.7713  lr=1.00e-03
23:36:37 [INFO] [me5-large_to_te3-small][deep] 13/15  train_loss=0.16292  test_loss=0.22688  test_cos=0.7731  lr=1.00e-03
23:36:48 [INFO] [me5-large_to_te3-small][deep] 14/15  train_loss=0.16245  test_loss=0.22476  test_cos=0.7752  lr=1.00e-03
23:36:59 [INFO] [me5-large_to_te3-small][deep] 15/15  train_loss=0.16200  test_loss=0.22284  test_cos=0.7772  lr=1.00e-03
23:36:59 [INFO] [me5-large_to_te3-small] winner=linear best_epoch=15 best_test_cos=0.7782 saved → me5-large_to_te3-small.pt  (354.2s)
23:36:59 [INFO]
─── [27/49] me5-large → qwen3-emb-8b ───
23:36:59 [INFO] [me5-large_to_qwen3-emb-8b] 1024d → 4096d
23:37:29 [INFO] [me5-large_to_qwen3-emb-8b][linear] 01/15  train_loss=0.22725  test_loss=0.30181  test_cos=0.6982  lr=1.00e-03
23:37:59 [INFO] [me5-large_to_qwen3-emb-8b][linear] 02/15  train_loss=0.20234  test_loss=0.28302  test_cos=0.7170  lr=1.00e-03
23:38:29 [INFO] [me5-large_to_qwen3-emb-8b][linear] 03/15  train_loss=0.19942  test_loss=0.27530  test_cos=0.7247  lr=1.00e-03
23:39:00 [INFO] [me5-large_to_qwen3-emb-8b][linear] 04/15  train_loss=0.19784  test_loss=0.27172  test_cos=0.7283  lr=1.00e-03
23:39:30 [INFO] [me5-large_to_qwen3-emb-8b][linear] 05/15  train_loss=0.19676  test_loss=0.27014  test_cos=0.7299  lr=1.00e-03
23:40:00 [INFO] [me5-large_to_qwen3-emb-8b][linear] 06/15  train_loss=0.19595  test_loss=0.26952  test_cos=0.7305  lr=1.00e-03
23:40:31 [INFO] [me5-large_to_qwen3-emb-8b][linear] 07/15  train_loss=0.19529  test_loss=0.26924  test_cos=0.7308  lr=1.00e-03
23:41:01 [INFO] [me5-large_to_qwen3-emb-8b][linear] 08/15  train_loss=0.19474  test_loss=0.26898  test_cos=0.7310  lr=1.00e-03
23:41:31 [INFO] [me5-large_to_qwen3-emb-8b][linear] 09/15  train_loss=0.19427  test_loss=0.26860  test_cos=0.7314  lr=1.00e-03
23:42:01 [INFO] [me5-large_to_qwen3-emb-8b][linear] 10/15  train_loss=0.19386  test_loss=0.26806  test_cos=0.7319  lr=1.00e-03
23:42:31 [INFO] [me5-large_to_qwen3-emb-8b][linear] 11/15  train_loss=0.19350  test_loss=0.26740  test_cos=0.7326  lr=1.00e-03
23:43:02 [INFO] [me5-large_to_qwen3-emb-8b][linear] 12/15  train_loss=0.19317  test_loss=0.26666  test_cos=0.7333  lr=1.00e-03
23:43:32 [INFO] [me5-large_to_qwen3-emb-8b][linear] 13/15  train_loss=0.19288  test_loss=0.26586  test_cos=0.7341  lr=1.00e-03
23:44:02 [INFO] [me5-large_to_qwen3-emb-8b][linear] 14/15  train_loss=0.19262  test_loss=0.26504  test_cos=0.7350  lr=1.00e-03
23:44:32 [INFO] [me5-large_to_qwen3-emb-8b][linear] 15/15  train_loss=0.19237  test_loss=0.26421  test_cos=0.7358  lr=1.00e-03
23:44:56 [INFO] [me5-large_to_qwen3-emb-8b][deep] 01/15  train_loss=0.25340  test_loss=0.34124  test_cos=0.6588  lr=1.00e-03
23:45:20 [INFO] [me5-large_to_qwen3-emb-8b][deep] 02/15  train_loss=0.20339  test_loss=0.30620  test_cos=0.6938  lr=1.00e-03
23:45:44 [INFO] [me5-large_to_qwen3-emb-8b][deep] 03/15  train_loss=0.19840  test_loss=0.29631  test_cos=0.7037  lr=1.00e-03
23:46:08 [INFO] [me5-large_to_qwen3-emb-8b][deep] 04/15  train_loss=0.19607  test_loss=0.29346  test_cos=0.7065  lr=1.00e-03
23:46:33 [INFO] [me5-large_to_qwen3-emb-8b][deep] 05/15  train_loss=0.19450  test_loss=0.28941  test_cos=0.7106  lr=1.00e-03
23:46:57 [INFO] [me5-large_to_qwen3-emb-8b][deep] 06/15  train_loss=0.19330  test_loss=0.28447  test_cos=0.7155  lr=1.00e-03
23:47:21 [INFO] [me5-large_to_qwen3-emb-8b][deep] 07/15  train_loss=0.19230  test_loss=0.28097  test_cos=0.7190  lr=1.00e-03
23:47:46 [INFO] [me5-large_to_qwen3-emb-8b][deep] 08/15  train_loss=0.19144  test_loss=0.27731  test_cos=0.7227  lr=1.00e-03
23:48:10 [INFO] [me5-large_to_qwen3-emb-8b][deep] 09/15  train_loss=0.19062  test_loss=0.27363  test_cos=0.7264  lr=1.00e-03
23:48:35 [INFO] [me5-large_to_qwen3-emb-8b][deep] 10/15  train_loss=0.18985  test_loss=0.27058  test_cos=0.7294  lr=1.00e-03
23:49:00 [INFO] [me5-large_to_qwen3-emb-8b][deep] 11/15  train_loss=0.18910  test_loss=0.26723  test_cos=0.7328  lr=1.00e-03
23:49:26 [INFO] [me5-large_to_qwen3-emb-8b][deep] 12/15  train_loss=0.18837  test_loss=0.26452  test_cos=0.7355  lr=1.00e-03
23:49:51 [INFO] [me5-large_to_qwen3-emb-8b][deep] 13/15  train_loss=0.18768  test_loss=0.26236  test_cos=0.7376  lr=1.00e-03
23:50:16 [INFO] [me5-large_to_qwen3-emb-8b][deep] 14/15  train_loss=0.18699  test_loss=0.26019  test_cos=0.7398  lr=1.00e-03
23:50:41 [INFO] [me5-large_to_qwen3-emb-8b][deep] 15/15  train_loss=0.18633  test_loss=0.25817  test_cos=0.7418  lr=1.00e-03
23:50:41 [INFO] [me5-large_to_qwen3-emb-8b] winner=deep best_epoch=15 best_test_cos=0.7418 saved → me5-large_to_qwen3-emb-8b.pt  (822.3s)
23:50:41 [INFO]
─── [28/49] me5-large → bge-m3 ───
23:50:41 [INFO] [me5-large_to_bge-m3] 1024d → 1024d
23:50:51 [INFO] [me5-large_to_bge-m3][linear] 01/15  train_loss=0.11810  test_loss=0.13294  test_cos=0.8671  lr=1.00e-03
23:51:01 [INFO] [me5-large_to_bge-m3][linear] 02/15  train_loss=0.09784  test_loss=0.12553  test_cos=0.8745  lr=1.00e-03
23:51:10 [INFO] [me5-large_to_bge-m3][linear] 03/15  train_loss=0.09633  test_loss=0.12287  test_cos=0.8771  lr=1.00e-03
23:51:20 [INFO] [me5-large_to_bge-m3][linear] 04/15  train_loss=0.09550  test_loss=0.12237  test_cos=0.8776  lr=1.00e-03
23:51:30 [INFO] [me5-large_to_bge-m3][linear] 05/15  train_loss=0.09493  test_loss=0.12289  test_cos=0.8771  lr=1.00e-03
23:51:40 [INFO] [me5-large_to_bge-m3][linear] 06/15  train_loss=0.09450  test_loss=0.12347  test_cos=0.8765  lr=1.00e-03
23:51:50 [INFO] [me5-large_to_bge-m3][linear] 07/15  train_loss=0.09415  test_loss=0.12367  test_cos=0.8763  lr=5.00e-04
23:52:00 [INFO] [me5-large_to_bge-m3][linear] 08/15  train_loss=0.09374  test_loss=0.11010  test_cos=0.8899  lr=5.00e-04
23:52:10 [INFO] [me5-large_to_bge-m3][linear] 09/15  train_loss=0.09294  test_loss=0.10980  test_cos=0.8902  lr=5.00e-04
23:52:20 [INFO] [me5-large_to_bge-m3][linear] 10/15  train_loss=0.09273  test_loss=0.10944  test_cos=0.8906  lr=5.00e-04
23:52:29 [INFO] [me5-large_to_bge-m3][linear] 11/15  train_loss=0.09258  test_loss=0.10912  test_cos=0.8909  lr=5.00e-04
23:52:39 [INFO] [me5-large_to_bge-m3][linear] 12/15  train_loss=0.09245  test_loss=0.10885  test_cos=0.8912  lr=5.00e-04
23:52:49 [INFO] [me5-large_to_bge-m3][linear] 13/15  train_loss=0.09233  test_loss=0.10861  test_cos=0.8914  lr=5.00e-04
23:52:58 [INFO] [me5-large_to_bge-m3][linear] 14/15  train_loss=0.09223  test_loss=0.10840  test_cos=0.8916  lr=5.00e-04
23:53:09 [INFO] [me5-large_to_bge-m3][linear] 15/15  train_loss=0.09214  test_loss=0.10822  test_cos=0.8918  lr=5.00e-04
23:53:19 [INFO] [me5-large_to_bge-m3][deep] 01/15  train_loss=0.13076  test_loss=0.14602  test_cos=0.8540  lr=1.00e-03
23:53:29 [INFO] [me5-large_to_bge-m3][deep] 02/15  train_loss=0.09888  test_loss=0.13394  test_cos=0.8661  lr=1.00e-03
23:53:39 [INFO] [me5-large_to_bge-m3][deep] 03/15  train_loss=0.09669  test_loss=0.12952  test_cos=0.8705  lr=1.00e-03
23:53:49 [INFO] [me5-large_to_bge-m3][deep] 04/15  train_loss=0.09558  test_loss=0.12725  test_cos=0.8728  lr=1.00e-03
23:53:59 [INFO] [me5-large_to_bge-m3][deep] 05/15  train_loss=0.09486  test_loss=0.12572  test_cos=0.8743  lr=1.00e-03
23:54:09 [INFO] [me5-large_to_bge-m3][deep] 06/15  train_loss=0.09434  test_loss=0.12406  test_cos=0.8759  lr=1.00e-03
23:54:20 [INFO] [me5-large_to_bge-m3][deep] 07/15  train_loss=0.09395  test_loss=0.12258  test_cos=0.8774  lr=1.00e-03
23:54:29 [INFO] [me5-large_to_bge-m3][deep] 08/15  train_loss=0.09363  test_loss=0.12120  test_cos=0.8788  lr=1.00e-03
23:54:39 [INFO] [me5-large_to_bge-m3][deep] 09/15  train_loss=0.09336  test_loss=0.11988  test_cos=0.8801  lr=1.00e-03
23:54:48 [INFO] [me5-large_to_bge-m3][deep] 10/15  train_loss=0.09314  test_loss=0.11910  test_cos=0.8809  lr=1.00e-03
23:54:58 [INFO] [me5-large_to_bge-m3][deep] 11/15  train_loss=0.09295  test_loss=0.11873  test_cos=0.8813  lr=1.00e-03
23:55:07 [INFO] [me5-large_to_bge-m3][deep] 12/15  train_loss=0.09277  test_loss=0.11855  test_cos=0.8814  lr=1.00e-03
23:55:17 [INFO] [me5-large_to_bge-m3][deep] 13/15  train_loss=0.09262  test_loss=0.11835  test_cos=0.8817  lr=1.00e-03
23:55:26 [INFO] [me5-large_to_bge-m3][deep] 14/15  train_loss=0.09248  test_loss=0.11802  test_cos=0.8820  lr=1.00e-03
23:55:36 [INFO] [me5-large_to_bge-m3][deep] 15/15  train_loss=0.09235  test_loss=0.11746  test_cos=0.8825  lr=1.00e-03
23:55:36 [INFO] [me5-large_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8918 saved → me5-large_to_bge-m3.pt  (294.2s)
23:55:36 [INFO]
─── [29/49] me5-large → pplx-embed-1 ───
23:55:36 [INFO] [me5-large_to_pplx-embed-1] 1024d → 1024d
23:55:45 [INFO] [me5-large_to_pplx-embed-1][linear] 01/15  train_loss=0.26849  test_loss=0.35921  test_cos=0.6408  lr=1.00e-03
23:55:54 [INFO] [me5-large_to_pplx-embed-1][linear] 02/15  train_loss=0.24121  test_loss=0.33478  test_cos=0.6652  lr=1.00e-03
23:56:04 [INFO] [me5-large_to_pplx-embed-1][linear] 03/15  train_loss=0.23772  test_loss=0.32383  test_cos=0.6762  lr=1.00e-03
23:56:13 [INFO] [me5-large_to_pplx-embed-1][linear] 04/15  train_loss=0.23577  test_loss=0.31647  test_cos=0.6835  lr=1.00e-03
23:56:23 [INFO] [me5-large_to_pplx-embed-1][linear] 05/15  train_loss=0.23440  test_loss=0.31089  test_cos=0.6891  lr=1.00e-03
23:56:32 [INFO] [me5-large_to_pplx-embed-1][linear] 06/15  train_loss=0.23335  test_loss=0.30658  test_cos=0.6934  lr=1.00e-03
23:56:42 [INFO] [me5-large_to_pplx-embed-1][linear] 07/15  train_loss=0.23250  test_loss=0.30320  test_cos=0.6968  lr=1.00e-03
23:56:51 [INFO] [me5-large_to_pplx-embed-1][linear] 08/15  train_loss=0.23179  test_loss=0.30051  test_cos=0.6995  lr=1.00e-03
23:57:00 [INFO] [me5-large_to_pplx-embed-1][linear] 09/15  train_loss=0.23118  test_loss=0.29830  test_cos=0.7017  lr=1.00e-03
23:57:10 [INFO] [me5-large_to_pplx-embed-1][linear] 10/15  train_loss=0.23065  test_loss=0.29644  test_cos=0.7036  lr=1.00e-03
23:57:19 [INFO] [me5-large_to_pplx-embed-1][linear] 11/15  train_loss=0.23019  test_loss=0.29484  test_cos=0.7052  lr=1.00e-03
23:57:28 [INFO] [me5-large_to_pplx-embed-1][linear] 12/15  train_loss=0.22977  test_loss=0.29342  test_cos=0.7066  lr=1.00e-03
23:57:38 [INFO] [me5-large_to_pplx-embed-1][linear] 13/15  train_loss=0.22939  test_loss=0.29213  test_cos=0.7079  lr=1.00e-03
23:57:47 [INFO] [me5-large_to_pplx-embed-1][linear] 14/15  train_loss=0.22905  test_loss=0.29096  test_cos=0.7090  lr=1.00e-03
23:57:56 [INFO] [me5-large_to_pplx-embed-1][linear] 15/15  train_loss=0.22874  test_loss=0.28987  test_cos=0.7101  lr=1.00e-03
23:58:06 [INFO] [me5-large_to_pplx-embed-1][deep] 01/15  train_loss=0.28593  test_loss=0.37893  test_cos=0.6211  lr=1.00e-03
23:58:15 [INFO] [me5-large_to_pplx-embed-1][deep] 02/15  train_loss=0.24032  test_loss=0.34556  test_cos=0.6544  lr=1.00e-03
23:58:25 [INFO] [me5-large_to_pplx-embed-1][deep] 03/15  train_loss=0.23576  test_loss=0.33439  test_cos=0.6656  lr=1.00e-03
23:58:34 [INFO] [me5-large_to_pplx-embed-1][deep] 04/15  train_loss=0.23344  test_loss=0.32635  test_cos=0.6737  lr=1.00e-03
23:58:44 [INFO] [me5-large_to_pplx-embed-1][deep] 05/15  train_loss=0.23186  test_loss=0.32041  test_cos=0.6796  lr=1.00e-03
23:58:53 [INFO] [me5-large_to_pplx-embed-1][deep] 06/15  train_loss=0.23066  test_loss=0.31661  test_cos=0.6834  lr=1.00e-03
23:59:02 [INFO] [me5-large_to_pplx-embed-1][deep] 07/15  train_loss=0.22968  test_loss=0.31231  test_cos=0.6877  lr=1.00e-03
23:59:12 [INFO] [me5-large_to_pplx-embed-1][deep] 08/15  train_loss=0.22880  test_loss=0.30838  test_cos=0.6916  lr=1.00e-03
23:59:21 [INFO] [me5-large_to_pplx-embed-1][deep] 09/15  train_loss=0.22798  test_loss=0.30573  test_cos=0.6943  lr=1.00e-03
23:59:31 [INFO] [me5-large_to_pplx-embed-1][deep] 10/15  train_loss=0.22723  test_loss=0.30284  test_cos=0.6972  lr=1.00e-03
23:59:40 [INFO] [me5-large_to_pplx-embed-1][deep] 11/15  train_loss=0.22649  test_loss=0.30011  test_cos=0.6999  lr=1.00e-03
23:59:50 [INFO] [me5-large_to_pplx-embed-1][deep] 12/15  train_loss=0.22577  test_loss=0.29766  test_cos=0.7023  lr=1.00e-03
23:59:59 [INFO] [me5-large_to_pplx-embed-1][deep] 13/15  train_loss=0.22506  test_loss=0.29557  test_cos=0.7044  lr=1.00e-03
00:00:09 [INFO] [me5-large_to_pplx-embed-1][deep] 14/15  train_loss=0.22438  test_loss=0.29358  test_cos=0.7064  lr=1.00e-03
00:00:18 [INFO] [me5-large_to_pplx-embed-1][deep] 15/15  train_loss=0.22370  test_loss=0.29142  test_cos=0.7086  lr=1.00e-03
00:00:18 [INFO] [me5-large_to_pplx-embed-1] winner=linear best_epoch=15 best_test_cos=0.7101 saved → me5-large_to_pplx-embed-1.pt  (282.3s)
00:00:18 [INFO]
─── [30/49] me5-large → nemotron-1b-free ───
00:00:18 [INFO] [me5-large_to_nemotron-1b-free] 1024d → 2048d
00:00:34 [INFO] [me5-large_to_nemotron-1b-free][linear] 01/15  train_loss=0.33223  test_loss=0.41427  test_cos=0.5857  lr=1.00e-03
00:00:49 [INFO] [me5-large_to_nemotron-1b-free][linear] 02/15  train_loss=0.29935  test_loss=0.39810  test_cos=0.6019  lr=1.00e-03
00:01:05 [INFO] [me5-large_to_nemotron-1b-free][linear] 03/15  train_loss=0.29526  test_loss=0.38765  test_cos=0.6124  lr=1.00e-03
00:01:21 [INFO] [me5-large_to_nemotron-1b-free][linear] 04/15  train_loss=0.29296  test_loss=0.38081  test_cos=0.6192  lr=1.00e-03
00:01:37 [INFO] [me5-large_to_nemotron-1b-free][linear] 05/15  train_loss=0.29135  test_loss=0.37618  test_cos=0.6238  lr=1.00e-03
00:01:52 [INFO] [me5-large_to_nemotron-1b-free][linear] 06/15  train_loss=0.29012  test_loss=0.37294  test_cos=0.6271  lr=1.00e-03
00:02:08 [INFO] [me5-large_to_nemotron-1b-free][linear] 07/15  train_loss=0.28913  test_loss=0.37056  test_cos=0.6294  lr=1.00e-03
00:02:24 [INFO] [me5-large_to_nemotron-1b-free][linear] 08/15  train_loss=0.28831  test_loss=0.36871  test_cos=0.6313  lr=1.00e-03
00:02:39 [INFO] [me5-large_to_nemotron-1b-free][linear] 09/15  train_loss=0.28761  test_loss=0.36718  test_cos=0.6328  lr=1.00e-03
00:02:55 [INFO] [me5-large_to_nemotron-1b-free][linear] 10/15  train_loss=0.28700  test_loss=0.36584  test_cos=0.6342  lr=1.00e-03
00:03:10 [INFO] [me5-large_to_nemotron-1b-free][linear] 11/15  train_loss=0.28646  test_loss=0.36463  test_cos=0.6354  lr=1.00e-03
00:03:26 [INFO] [me5-large_to_nemotron-1b-free][linear] 12/15  train_loss=0.28598  test_loss=0.36351  test_cos=0.6365  lr=1.00e-03
00:03:42 [INFO] [me5-large_to_nemotron-1b-free][linear] 13/15  train_loss=0.28555  test_loss=0.36245  test_cos=0.6375  lr=1.00e-03
00:03:57 [INFO] [me5-large_to_nemotron-1b-free][linear] 14/15  train_loss=0.28516  test_loss=0.36144  test_cos=0.6386  lr=1.00e-03
00:04:13 [INFO] [me5-large_to_nemotron-1b-free][linear] 15/15  train_loss=0.28480  test_loss=0.36047  test_cos=0.6395  lr=1.00e-03
00:04:27 [INFO] [me5-large_to_nemotron-1b-free][deep] 01/15  train_loss=0.36530  test_loss=0.43512  test_cos=0.5649  lr=1.00e-03
00:04:41 [INFO] [me5-large_to_nemotron-1b-free][deep] 02/15  train_loss=0.30218  test_loss=0.40354  test_cos=0.5965  lr=1.00e-03
00:04:55 [INFO] [me5-large_to_nemotron-1b-free][deep] 03/15  train_loss=0.29617  test_loss=0.39323  test_cos=0.6068  lr=1.00e-03
00:05:09 [INFO] [me5-large_to_nemotron-1b-free][deep] 04/15  train_loss=0.29328  test_loss=0.38687  test_cos=0.6131  lr=1.00e-03
00:05:23 [INFO] [me5-large_to_nemotron-1b-free][deep] 05/15  train_loss=0.29149  test_loss=0.38355  test_cos=0.6164  lr=1.00e-03
00:05:36 [INFO] [me5-large_to_nemotron-1b-free][deep] 06/15  train_loss=0.29020  test_loss=0.37856  test_cos=0.6214  lr=1.00e-03
00:05:50 [INFO] [me5-large_to_nemotron-1b-free][deep] 07/15  train_loss=0.28921  test_loss=0.37319  test_cos=0.6268  lr=1.00e-03
00:06:04 [INFO] [me5-large_to_nemotron-1b-free][deep] 08/15  train_loss=0.28841  test_loss=0.36866  test_cos=0.6313  lr=1.00e-03
00:06:18 [INFO] [me5-large_to_nemotron-1b-free][deep] 09/15  train_loss=0.28771  test_loss=0.36513  test_cos=0.6349  lr=1.00e-03
00:06:32 [INFO] [me5-large_to_nemotron-1b-free][deep] 10/15  train_loss=0.28711  test_loss=0.36241  test_cos=0.6376  lr=1.00e-03
00:06:46 [INFO] [me5-large_to_nemotron-1b-free][deep] 11/15  train_loss=0.28658  test_loss=0.36063  test_cos=0.6394  lr=1.00e-03
00:07:00 [INFO] [me5-large_to_nemotron-1b-free][deep] 12/15  train_loss=0.28611  test_loss=0.35950  test_cos=0.6405  lr=1.00e-03
00:07:13 [INFO] [me5-large_to_nemotron-1b-free][deep] 13/15  train_loss=0.28566  test_loss=0.35849  test_cos=0.6415  lr=1.00e-03
00:07:27 [INFO] [me5-large_to_nemotron-1b-free][deep] 14/15  train_loss=0.28525  test_loss=0.35738  test_cos=0.6426  lr=1.00e-03
00:07:41 [INFO] [me5-large_to_nemotron-1b-free][deep] 15/15  train_loss=0.28487  test_loss=0.35604  test_cos=0.6440  lr=1.00e-03
00:07:41 [INFO] [me5-large_to_nemotron-1b-free] winner=deep best_epoch=15 best_test_cos=0.6440 saved → me5-large_to_nemotron-1b-free.pt  (443.3s)
00:07:41 [INFO]
─── [31/49] me5-large → fastembed-bge-small ───
00:07:41 [INFO] [me5-large_to_fastembed-bge-small] 1024d → 384d
00:07:47 [INFO] [me5-large_to_fastembed-bge-small][linear] 01/15  train_loss=0.09155  test_loss=0.13529  test_cos=0.8647  lr=1.00e-03
00:07:52 [INFO] [me5-large_to_fastembed-bge-small][linear] 02/15  train_loss=0.08166  test_loss=0.12619  test_cos=0.8738  lr=1.00e-03
00:07:58 [INFO] [me5-large_to_fastembed-bge-small][linear] 03/15  train_loss=0.08053  test_loss=0.12061  test_cos=0.8794  lr=1.00e-03
00:08:03 [INFO] [me5-large_to_fastembed-bge-small][linear] 04/15  train_loss=0.07991  test_loss=0.11542  test_cos=0.8846  lr=1.00e-03
00:08:09 [INFO] [me5-large_to_fastembed-bge-small][linear] 05/15  train_loss=0.07947  test_loss=0.11123  test_cos=0.8888  lr=1.00e-03
00:08:14 [INFO] [me5-large_to_fastembed-bge-small][linear] 06/15  train_loss=0.07914  test_loss=0.10814  test_cos=0.8919  lr=1.00e-03
00:08:20 [INFO] [me5-large_to_fastembed-bge-small][linear] 07/15  train_loss=0.07887  test_loss=0.10591  test_cos=0.8941  lr=1.00e-03
00:08:25 [INFO] [me5-large_to_fastembed-bge-small][linear] 08/15  train_loss=0.07864  test_loss=0.10430  test_cos=0.8957  lr=1.00e-03
00:08:31 [INFO] [me5-large_to_fastembed-bge-small][linear] 09/15  train_loss=0.07845  test_loss=0.10316  test_cos=0.8968  lr=1.00e-03
00:08:37 [INFO] [me5-large_to_fastembed-bge-small][linear] 10/15  train_loss=0.07829  test_loss=0.10235  test_cos=0.8976  lr=1.00e-03
00:08:42 [INFO] [me5-large_to_fastembed-bge-small][linear] 11/15  train_loss=0.07814  test_loss=0.10180  test_cos=0.8982  lr=1.00e-03
00:08:48 [INFO] [me5-large_to_fastembed-bge-small][linear] 12/15  train_loss=0.07801  test_loss=0.10143  test_cos=0.8986  lr=1.00e-03
00:08:53 [INFO] [me5-large_to_fastembed-bge-small][linear] 13/15  train_loss=0.07790  test_loss=0.10120  test_cos=0.8988  lr=1.00e-03
00:08:59 [INFO] [me5-large_to_fastembed-bge-small][linear] 14/15  train_loss=0.07779  test_loss=0.10109  test_cos=0.8989  lr=1.00e-03
00:09:04 [INFO] [me5-large_to_fastembed-bge-small][linear] 15/15  train_loss=0.07770  test_loss=0.10104  test_cos=0.8990  lr=1.00e-03
00:09:10 [INFO] [me5-large_to_fastembed-bge-small][deep] 01/15  train_loss=0.10555  test_loss=0.15462  test_cos=0.8454  lr=1.00e-03
00:09:16 [INFO] [me5-large_to_fastembed-bge-small][deep] 02/15  train_loss=0.08526  test_loss=0.13537  test_cos=0.8646  lr=1.00e-03
00:09:21 [INFO] [me5-large_to_fastembed-bge-small][deep] 03/15  train_loss=0.08345  test_loss=0.12862  test_cos=0.8714  lr=1.00e-03
00:09:26 [INFO] [me5-large_to_fastembed-bge-small][deep] 04/15  train_loss=0.08270  test_loss=0.12517  test_cos=0.8748  lr=1.00e-03
00:09:31 [INFO] [me5-large_to_fastembed-bge-small][deep] 05/15  train_loss=0.08226  test_loss=0.12267  test_cos=0.8773  lr=1.00e-03
00:09:36 [INFO] [me5-large_to_fastembed-bge-small][deep] 06/15  train_loss=0.08197  test_loss=0.12109  test_cos=0.8789  lr=1.00e-03
00:09:42 [INFO] [me5-large_to_fastembed-bge-small][deep] 07/15  train_loss=0.08175  test_loss=0.12023  test_cos=0.8798  lr=1.00e-03
00:09:47 [INFO] [me5-large_to_fastembed-bge-small][deep] 08/15  train_loss=0.08157  test_loss=0.11945  test_cos=0.8806  lr=1.00e-03
00:09:52 [INFO] [me5-large_to_fastembed-bge-small][deep] 09/15  train_loss=0.08145  test_loss=0.11799  test_cos=0.8820  lr=1.00e-03
00:09:57 [INFO] [me5-large_to_fastembed-bge-small][deep] 10/15  train_loss=0.08126  test_loss=0.11678  test_cos=0.8832  lr=1.00e-03
00:10:03 [INFO] [me5-large_to_fastembed-bge-small][deep] 11/15  train_loss=0.08112  test_loss=0.11570  test_cos=0.8843  lr=1.00e-03
00:10:08 [INFO] [me5-large_to_fastembed-bge-small][deep] 12/15  train_loss=0.08099  test_loss=0.11464  test_cos=0.8854  lr=1.00e-03
00:10:13 [INFO] [me5-large_to_fastembed-bge-small][deep] 13/15  train_loss=0.08088  test_loss=0.11360  test_cos=0.8864  lr=1.00e-03
00:10:18 [INFO] [me5-large_to_fastembed-bge-small][deep] 14/15  train_loss=0.08077  test_loss=0.11257  test_cos=0.8874  lr=1.00e-03
00:10:23 [INFO] [me5-large_to_fastembed-bge-small][deep] 15/15  train_loss=0.08066  test_loss=0.11159  test_cos=0.8884  lr=1.00e-03
00:10:23 [INFO] [me5-large_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.8990 saved → me5-large_to_fastembed-bge-small.pt  (162.1s)
00:10:23 [INFO]
─── [32/49] pplx-embed-1 → te3-small ───
00:10:23 [INFO] [pplx-embed-1_to_te3-small] 1024d → 1536d
00:10:36 [INFO] [pplx-embed-1_to_te3-small][linear] 01/15  train_loss=0.15364  test_loss=0.22760  test_cos=0.7724  lr=1.00e-03
00:10:49 [INFO] [pplx-embed-1_to_te3-small][linear] 02/15  train_loss=0.14200  test_loss=0.21121  test_cos=0.7888  lr=1.00e-03
00:11:01 [INFO] [pplx-embed-1_to_te3-small][linear] 03/15  train_loss=0.14115  test_loss=0.20316  test_cos=0.7968  lr=1.00e-03
00:11:14 [INFO] [pplx-embed-1_to_te3-small][linear] 04/15  train_loss=0.14085  test_loss=0.19744  test_cos=0.8026  lr=1.00e-03
00:11:26 [INFO] [pplx-embed-1_to_te3-small][linear] 05/15  train_loss=0.14070  test_loss=0.19295  test_cos=0.8070  lr=1.00e-03
00:11:39 [INFO] [pplx-embed-1_to_te3-small][linear] 06/15  train_loss=0.14061  test_loss=0.18930  test_cos=0.8107  lr=1.00e-03
00:11:51 [INFO] [pplx-embed-1_to_te3-small][linear] 07/15  train_loss=0.14055  test_loss=0.18627  test_cos=0.8137  lr=1.00e-03
00:12:04 [INFO] [pplx-embed-1_to_te3-small][linear] 08/15  train_loss=0.14051  test_loss=0.18370  test_cos=0.8163  lr=1.00e-03
00:12:16 [INFO] [pplx-embed-1_to_te3-small][linear] 09/15  train_loss=0.14048  test_loss=0.18151  test_cos=0.8185  lr=1.00e-03
00:12:29 [INFO] [pplx-embed-1_to_te3-small][linear] 10/15  train_loss=0.14046  test_loss=0.17961  test_cos=0.8204  lr=1.00e-03
00:12:41 [INFO] [pplx-embed-1_to_te3-small][linear] 11/15  train_loss=0.14045  test_loss=0.17795  test_cos=0.8221  lr=1.00e-03
00:12:53 [INFO] [pplx-embed-1_to_te3-small][linear] 12/15  train_loss=0.14044  test_loss=0.17647  test_cos=0.8235  lr=1.00e-03
00:13:06 [INFO] [pplx-embed-1_to_te3-small][linear] 13/15  train_loss=0.14043  test_loss=0.17516  test_cos=0.8248  lr=1.00e-03
00:13:18 [INFO] [pplx-embed-1_to_te3-small][linear] 14/15  train_loss=0.14042  test_loss=0.17398  test_cos=0.8260  lr=1.00e-03
00:13:31 [INFO] [pplx-embed-1_to_te3-small][linear] 15/15  train_loss=0.14042  test_loss=0.17291  test_cos=0.8271  lr=1.00e-03
00:13:42 [INFO] [pplx-embed-1_to_te3-small][deep] 01/15  train_loss=0.17019  test_loss=0.25636  test_cos=0.7436  lr=1.00e-03
00:13:54 [INFO] [pplx-embed-1_to_te3-small][deep] 02/15  train_loss=0.14695  test_loss=0.23476  test_cos=0.7652  lr=1.00e-03
00:14:05 [INFO] [pplx-embed-1_to_te3-small][deep] 03/15  train_loss=0.14484  test_loss=0.22393  test_cos=0.7761  lr=1.00e-03
00:14:17 [INFO] [pplx-embed-1_to_te3-small][deep] 04/15  train_loss=0.14392  test_loss=0.21692  test_cos=0.7831  lr=1.00e-03
00:14:29 [INFO] [pplx-embed-1_to_te3-small][deep] 05/15  train_loss=0.14334  test_loss=0.21139  test_cos=0.7886  lr=1.00e-03
00:14:40 [INFO] [pplx-embed-1_to_te3-small][deep] 06/15  train_loss=0.14290  test_loss=0.20691  test_cos=0.7931  lr=1.00e-03
00:14:52 [INFO] [pplx-embed-1_to_te3-small][deep] 07/15  train_loss=0.14252  test_loss=0.20310  test_cos=0.7969  lr=1.00e-03
00:15:04 [INFO] [pplx-embed-1_to_te3-small][deep] 08/15  train_loss=0.14217  test_loss=0.19982  test_cos=0.8002  lr=1.00e-03
00:15:16 [INFO] [pplx-embed-1_to_te3-small][deep] 09/15  train_loss=0.14183  test_loss=0.19692  test_cos=0.8031  lr=1.00e-03
00:15:27 [INFO] [pplx-embed-1_to_te3-small][deep] 10/15  train_loss=0.14149  test_loss=0.19437  test_cos=0.8056  lr=1.00e-03
00:15:39 [INFO] [pplx-embed-1_to_te3-small][deep] 11/15  train_loss=0.14115  test_loss=0.19208  test_cos=0.8079  lr=1.00e-03
00:15:50 [INFO] [pplx-embed-1_to_te3-small][deep] 12/15  train_loss=0.14081  test_loss=0.18999  test_cos=0.8100  lr=1.00e-03
00:16:02 [INFO] [pplx-embed-1_to_te3-small][deep] 13/15  train_loss=0.14048  test_loss=0.18810  test_cos=0.8119  lr=1.00e-03
00:16:13 [INFO] [pplx-embed-1_to_te3-small][deep] 14/15  train_loss=0.14014  test_loss=0.18635  test_cos=0.8136  lr=1.00e-03
00:16:25 [INFO] [pplx-embed-1_to_te3-small][deep] 15/15  train_loss=0.13981  test_loss=0.18474  test_cos=0.8153  lr=1.00e-03
00:16:25 [INFO] [pplx-embed-1_to_te3-small] winner=linear best_epoch=15 best_test_cos=0.8271 saved → pplx-embed-1_to_te3-small.pt  (361.6s)
00:16:25 [INFO]
─── [33/49] pplx-embed-1 → qwen3-emb-8b ───
00:16:25 [INFO] [pplx-embed-1_to_qwen3-emb-8b] 1024d → 4096d
00:16:56 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 01/15  train_loss=0.16995  test_loss=0.27440  test_cos=0.7256  lr=1.00e-03
00:17:27 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 02/15  train_loss=0.15806  test_loss=0.25395  test_cos=0.7461  lr=1.00e-03
00:17:58 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 03/15  train_loss=0.15714  test_loss=0.24343  test_cos=0.7566  lr=1.00e-03
00:18:30 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 04/15  train_loss=0.15687  test_loss=0.23584  test_cos=0.7642  lr=1.00e-03
00:19:01 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 05/15  train_loss=0.15677  test_loss=0.22985  test_cos=0.7701  lr=1.00e-03
00:19:32 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 06/15  train_loss=0.15673  test_loss=0.22497  test_cos=0.7750  lr=1.00e-03
00:20:03 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 07/15  train_loss=0.15671  test_loss=0.22090  test_cos=0.7791  lr=1.00e-03
00:20:33 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 08/15  train_loss=0.15672  test_loss=0.21746  test_cos=0.7825  lr=1.00e-03
00:21:03 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 09/15  train_loss=0.15673  test_loss=0.21451  test_cos=0.7855  lr=1.00e-03
00:21:32 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 10/15  train_loss=0.15674  test_loss=0.21194  test_cos=0.7881  lr=1.00e-03
00:22:02 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 11/15  train_loss=0.15676  test_loss=0.20968  test_cos=0.7903  lr=1.00e-03
00:22:31 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 12/15  train_loss=0.15678  test_loss=0.20768  test_cos=0.7923  lr=1.00e-03
00:23:00 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 13/15  train_loss=0.15680  test_loss=0.20588  test_cos=0.7941  lr=1.00e-03
00:23:29 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 14/15  train_loss=0.15681  test_loss=0.20426  test_cos=0.7957  lr=1.00e-03
00:23:58 [INFO] [pplx-embed-1_to_qwen3-emb-8b][linear] 15/15  train_loss=0.15683  test_loss=0.20278  test_cos=0.7972  lr=1.00e-03
00:24:22 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 01/15  train_loss=0.19479  test_loss=0.29692  test_cos=0.7031  lr=1.00e-03
00:24:44 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 02/15  train_loss=0.16567  test_loss=0.27309  test_cos=0.7269  lr=1.00e-03
00:25:07 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 03/15  train_loss=0.16329  test_loss=0.26253  test_cos=0.7375  lr=1.00e-03
00:25:30 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 04/15  train_loss=0.16242  test_loss=0.25499  test_cos=0.7450  lr=1.00e-03
00:25:53 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 05/15  train_loss=0.16188  test_loss=0.24912  test_cos=0.7509  lr=1.00e-03
00:26:16 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 06/15  train_loss=0.16145  test_loss=0.24392  test_cos=0.7561  lr=1.00e-03
00:26:39 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 07/15  train_loss=0.16105  test_loss=0.23911  test_cos=0.7609  lr=1.00e-03
00:27:02 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 08/15  train_loss=0.16068  test_loss=0.23476  test_cos=0.7652  lr=1.00e-03
00:27:25 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 09/15  train_loss=0.16031  test_loss=0.23093  test_cos=0.7691  lr=1.00e-03
00:27:48 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 10/15  train_loss=0.15995  test_loss=0.22756  test_cos=0.7724  lr=1.00e-03
00:28:10 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 11/15  train_loss=0.15960  test_loss=0.22459  test_cos=0.7754  lr=1.00e-03
00:28:33 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 12/15  train_loss=0.15926  test_loss=0.22193  test_cos=0.7781  lr=1.00e-03
00:28:56 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 13/15  train_loss=0.15892  test_loss=0.21950  test_cos=0.7805  lr=1.00e-03
00:29:19 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 14/15  train_loss=0.15859  test_loss=0.21725  test_cos=0.7827  lr=1.00e-03
00:29:42 [INFO] [pplx-embed-1_to_qwen3-emb-8b][deep] 15/15  train_loss=0.15828  test_loss=0.21516  test_cos=0.7848  lr=1.00e-03
00:29:42 [INFO] [pplx-embed-1_to_qwen3-emb-8b] winner=linear best_epoch=15 best_test_cos=0.7972 saved → pplx-embed-1_to_qwen3-emb-8b.pt  (796.7s)
00:29:42 [INFO]
─── [34/49] pplx-embed-1 → bge-m3 ───
00:29:42 [INFO] [pplx-embed-1_to_bge-m3] 1024d → 1024d
00:29:51 [INFO] [pplx-embed-1_to_bge-m3][linear] 01/15  train_loss=0.13117  test_loss=0.16792  test_cos=0.8321  lr=1.00e-03
00:30:00 [INFO] [pplx-embed-1_to_bge-m3][linear] 02/15  train_loss=0.12004  test_loss=0.15770  test_cos=0.8423  lr=1.00e-03
00:30:09 [INFO] [pplx-embed-1_to_bge-m3][linear] 03/15  train_loss=0.11923  test_loss=0.15286  test_cos=0.8471  lr=1.00e-03
00:30:17 [INFO] [pplx-embed-1_to_bge-m3][linear] 04/15  train_loss=0.11894  test_loss=0.14953  test_cos=0.8505  lr=1.00e-03
00:30:26 [INFO] [pplx-embed-1_to_bge-m3][linear] 05/15  train_loss=0.11878  test_loss=0.14697  test_cos=0.8530  lr=1.00e-03
00:30:35 [INFO] [pplx-embed-1_to_bge-m3][linear] 06/15  train_loss=0.11869  test_loss=0.14491  test_cos=0.8551  lr=1.00e-03
00:30:44 [INFO] [pplx-embed-1_to_bge-m3][linear] 07/15  train_loss=0.11864  test_loss=0.14322  test_cos=0.8568  lr=1.00e-03
00:30:53 [INFO] [pplx-embed-1_to_bge-m3][linear] 08/15  train_loss=0.11860  test_loss=0.14181  test_cos=0.8582  lr=1.00e-03
00:31:01 [INFO] [pplx-embed-1_to_bge-m3][linear] 09/15  train_loss=0.11857  test_loss=0.14060  test_cos=0.8594  lr=1.00e-03
00:31:10 [INFO] [pplx-embed-1_to_bge-m3][linear] 10/15  train_loss=0.11855  test_loss=0.13957  test_cos=0.8604  lr=1.00e-03
00:31:19 [INFO] [pplx-embed-1_to_bge-m3][linear] 11/15  train_loss=0.11853  test_loss=0.13868  test_cos=0.8613  lr=1.00e-03
00:31:27 [INFO] [pplx-embed-1_to_bge-m3][linear] 12/15  train_loss=0.11852  test_loss=0.13789  test_cos=0.8621  lr=1.00e-03
00:31:36 [INFO] [pplx-embed-1_to_bge-m3][linear] 13/15  train_loss=0.11851  test_loss=0.13720  test_cos=0.8628  lr=1.00e-03
00:31:45 [INFO] [pplx-embed-1_to_bge-m3][linear] 14/15  train_loss=0.11851  test_loss=0.13657  test_cos=0.8634  lr=1.00e-03
00:31:53 [INFO] [pplx-embed-1_to_bge-m3][linear] 15/15  train_loss=0.11850  test_loss=0.13601  test_cos=0.8640  lr=1.00e-03
00:32:02 [INFO] [pplx-embed-1_to_bge-m3][deep] 01/15  train_loss=0.13842  test_loss=0.17760  test_cos=0.8224  lr=1.00e-03
00:32:11 [INFO] [pplx-embed-1_to_bge-m3][deep] 02/15  train_loss=0.12165  test_loss=0.16604  test_cos=0.8340  lr=1.00e-03
00:32:20 [INFO] [pplx-embed-1_to_bge-m3][deep] 03/15  train_loss=0.12034  test_loss=0.16077  test_cos=0.8392  lr=1.00e-03
00:32:29 [INFO] [pplx-embed-1_to_bge-m3][deep] 04/15  train_loss=0.11972  test_loss=0.15718  test_cos=0.8428  lr=1.00e-03
00:32:38 [INFO] [pplx-embed-1_to_bge-m3][deep] 05/15  train_loss=0.11932  test_loss=0.15444  test_cos=0.8456  lr=1.00e-03
00:32:47 [INFO] [pplx-embed-1_to_bge-m3][deep] 06/15  train_loss=0.11902  test_loss=0.15225  test_cos=0.8478  lr=1.00e-03
00:32:56 [INFO] [pplx-embed-1_to_bge-m3][deep] 07/15  train_loss=0.11877  test_loss=0.15043  test_cos=0.8496  lr=1.00e-03
00:33:04 [INFO] [pplx-embed-1_to_bge-m3][deep] 08/15  train_loss=0.11855  test_loss=0.14885  test_cos=0.8511  lr=1.00e-03
00:33:13 [INFO] [pplx-embed-1_to_bge-m3][deep] 09/15  train_loss=0.11835  test_loss=0.14746  test_cos=0.8525  lr=1.00e-03
00:33:22 [INFO] [pplx-embed-1_to_bge-m3][deep] 10/15  train_loss=0.11816  test_loss=0.14621  test_cos=0.8538  lr=1.00e-03
00:33:31 [INFO] [pplx-embed-1_to_bge-m3][deep] 11/15  train_loss=0.11797  test_loss=0.14507  test_cos=0.8549  lr=1.00e-03
00:33:40 [INFO] [pplx-embed-1_to_bge-m3][deep] 12/15  train_loss=0.11778  test_loss=0.14403  test_cos=0.8560  lr=1.00e-03
00:33:49 [INFO] [pplx-embed-1_to_bge-m3][deep] 13/15  train_loss=0.11759  test_loss=0.14306  test_cos=0.8569  lr=1.00e-03
00:33:58 [INFO] [pplx-embed-1_to_bge-m3][deep] 14/15  train_loss=0.11740  test_loss=0.14216  test_cos=0.8578  lr=1.00e-03
00:34:07 [INFO] [pplx-embed-1_to_bge-m3][deep] 15/15  train_loss=0.11721  test_loss=0.14131  test_cos=0.8587  lr=1.00e-03
00:34:07 [INFO] [pplx-embed-1_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8640 saved → pplx-embed-1_to_bge-m3.pt  (265.2s)
00:34:07 [INFO]
─── [35/49] pplx-embed-1 → me5-large ───
00:34:07 [INFO] [pplx-embed-1_to_me5-large] 1024d → 1024d
00:34:16 [INFO] [pplx-embed-1_to_me5-large][linear] 01/15  train_loss=0.05329  test_loss=0.07134  test_cos=0.9287  lr=1.00e-03
00:34:25 [INFO] [pplx-embed-1_to_me5-large][linear] 02/15  train_loss=0.04694  test_loss=0.06681  test_cos=0.9332  lr=1.00e-03
00:34:34 [INFO] [pplx-embed-1_to_me5-large][linear] 03/15  train_loss=0.04637  test_loss=0.06501  test_cos=0.9350  lr=1.00e-03
00:34:42 [INFO] [pplx-embed-1_to_me5-large][linear] 04/15  train_loss=0.04620  test_loss=0.06359  test_cos=0.9364  lr=1.00e-03
00:34:51 [INFO] [pplx-embed-1_to_me5-large][linear] 05/15  train_loss=0.04611  test_loss=0.06244  test_cos=0.9376  lr=1.00e-03
00:35:00 [INFO] [pplx-embed-1_to_me5-large][linear] 06/15  train_loss=0.04605  test_loss=0.06150  test_cos=0.9385  lr=1.00e-03
00:35:09 [INFO] [pplx-embed-1_to_me5-large][linear] 07/15  train_loss=0.04602  test_loss=0.06071  test_cos=0.9393  lr=1.00e-03
00:35:17 [INFO] [pplx-embed-1_to_me5-large][linear] 08/15  train_loss=0.04600  test_loss=0.06005  test_cos=0.9399  lr=1.00e-03
00:35:26 [INFO] [pplx-embed-1_to_me5-large][linear] 09/15  train_loss=0.04598  test_loss=0.05949  test_cos=0.9405  lr=1.00e-03
00:35:35 [INFO] [pplx-embed-1_to_me5-large][linear] 10/15  train_loss=0.04597  test_loss=0.05902  test_cos=0.9410  lr=1.00e-03
00:35:44 [INFO] [pplx-embed-1_to_me5-large][linear] 11/15  train_loss=0.04596  test_loss=0.05860  test_cos=0.9414  lr=1.00e-03
00:35:52 [INFO] [pplx-embed-1_to_me5-large][linear] 12/15  train_loss=0.04595  test_loss=0.05825  test_cos=0.9418  lr=1.00e-03
00:36:01 [INFO] [pplx-embed-1_to_me5-large][linear] 13/15  train_loss=0.04595  test_loss=0.05793  test_cos=0.9421  lr=1.00e-03
00:36:10 [INFO] [pplx-embed-1_to_me5-large][linear] 14/15  train_loss=0.04594  test_loss=0.05765  test_cos=0.9424  lr=1.00e-03
00:36:19 [INFO] [pplx-embed-1_to_me5-large][linear] 15/15  train_loss=0.04594  test_loss=0.05739  test_cos=0.9426  lr=1.00e-03
00:36:28 [INFO] [pplx-embed-1_to_me5-large][deep] 01/15  train_loss=0.05692  test_loss=0.07944  test_cos=0.9206  lr=1.00e-03
00:36:36 [INFO] [pplx-embed-1_to_me5-large][deep] 02/15  train_loss=0.04753  test_loss=0.07309  test_cos=0.9269  lr=1.00e-03
00:36:45 [INFO] [pplx-embed-1_to_me5-large][deep] 03/15  train_loss=0.04689  test_loss=0.06999  test_cos=0.9300  lr=1.00e-03
00:36:54 [INFO] [pplx-embed-1_to_me5-large][deep] 04/15  train_loss=0.04661  test_loss=0.06803  test_cos=0.9320  lr=1.00e-03
00:37:03 [INFO] [pplx-embed-1_to_me5-large][deep] 05/15  train_loss=0.04644  test_loss=0.06646  test_cos=0.9335  lr=1.00e-03
00:37:12 [INFO] [pplx-embed-1_to_me5-large][deep] 06/15  train_loss=0.04633  test_loss=0.06525  test_cos=0.9348  lr=1.00e-03
00:37:21 [INFO] [pplx-embed-1_to_me5-large][deep] 07/15  train_loss=0.04624  test_loss=0.06425  test_cos=0.9358  lr=1.00e-03
00:37:29 [INFO] [pplx-embed-1_to_me5-large][deep] 08/15  train_loss=0.04617  test_loss=0.06349  test_cos=0.9365  lr=1.00e-03
00:37:38 [INFO] [pplx-embed-1_to_me5-large][deep] 09/15  train_loss=0.04611  test_loss=0.06283  test_cos=0.9372  lr=1.00e-03
00:37:47 [INFO] [pplx-embed-1_to_me5-large][deep] 10/15  train_loss=0.04605  test_loss=0.06229  test_cos=0.9377  lr=1.00e-03
00:37:56 [INFO] [pplx-embed-1_to_me5-large][deep] 11/15  train_loss=0.04600  test_loss=0.06181  test_cos=0.9382  lr=1.00e-03
00:38:05 [INFO] [pplx-embed-1_to_me5-large][deep] 12/15  train_loss=0.04595  test_loss=0.06140  test_cos=0.9386  lr=1.00e-03
00:38:14 [INFO] [pplx-embed-1_to_me5-large][deep] 13/15  train_loss=0.04590  test_loss=0.06103  test_cos=0.9390  lr=1.00e-03
00:38:22 [INFO] [pplx-embed-1_to_me5-large][deep] 14/15  train_loss=0.04585  test_loss=0.06069  test_cos=0.9393  lr=1.00e-03
00:38:31 [INFO] [pplx-embed-1_to_me5-large][deep] 15/15  train_loss=0.04580  test_loss=0.06038  test_cos=0.9396  lr=1.00e-03
00:38:31 [INFO] [pplx-embed-1_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9426 saved → pplx-embed-1_to_me5-large.pt  (264.4s)
00:38:31 [INFO]
─── [36/49] pplx-embed-1 → nemotron-1b-free ───
00:38:31 [INFO] [pplx-embed-1_to_nemotron-1b-free] 1024d → 2048d
00:38:46 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 01/15  train_loss=0.27307  test_loss=0.35942  test_cos=0.6406  lr=1.00e-03
00:39:01 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 02/15  train_loss=0.25699  test_loss=0.34197  test_cos=0.6580  lr=1.00e-03
00:39:16 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 03/15  train_loss=0.25567  test_loss=0.33289  test_cos=0.6671  lr=1.00e-03
00:39:31 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 04/15  train_loss=0.25512  test_loss=0.32639  test_cos=0.6736  lr=1.00e-03
00:39:45 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 05/15  train_loss=0.25481  test_loss=0.32126  test_cos=0.6787  lr=1.00e-03
00:40:00 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 06/15  train_loss=0.25460  test_loss=0.31703  test_cos=0.6830  lr=1.00e-03
00:40:15 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 07/15  train_loss=0.25446  test_loss=0.31349  test_cos=0.6865  lr=1.00e-03
00:40:30 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 08/15  train_loss=0.25435  test_loss=0.31047  test_cos=0.6895  lr=1.00e-03
00:40:45 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 09/15  train_loss=0.25427  test_loss=0.30787  test_cos=0.6921  lr=1.00e-03
00:41:00 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 10/15  train_loss=0.25421  test_loss=0.30560  test_cos=0.6944  lr=1.00e-03
00:41:14 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 11/15  train_loss=0.25416  test_loss=0.30360  test_cos=0.6964  lr=1.00e-03
00:41:29 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 12/15  train_loss=0.25411  test_loss=0.30182  test_cos=0.6982  lr=1.00e-03
00:41:44 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 13/15  train_loss=0.25408  test_loss=0.30022  test_cos=0.6998  lr=1.00e-03
00:41:58 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 14/15  train_loss=0.25405  test_loss=0.29878  test_cos=0.7012  lr=1.00e-03
00:42:13 [INFO] [pplx-embed-1_to_nemotron-1b-free][linear] 15/15  train_loss=0.25402  test_loss=0.29746  test_cos=0.7025  lr=1.00e-03
00:42:26 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 01/15  train_loss=0.29870  test_loss=0.38660  test_cos=0.6134  lr=1.00e-03
00:42:39 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 02/15  train_loss=0.26713  test_loss=0.36487  test_cos=0.6351  lr=1.00e-03
00:42:52 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 03/15  train_loss=0.26471  test_loss=0.35418  test_cos=0.6458  lr=1.00e-03
00:43:05 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 04/15  train_loss=0.26384  test_loss=0.34675  test_cos=0.6533  lr=1.00e-03
00:43:18 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 05/15  train_loss=0.26339  test_loss=0.34125  test_cos=0.6587  lr=1.00e-03
00:43:31 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 06/15  train_loss=0.26309  test_loss=0.33685  test_cos=0.6631  lr=1.00e-03
00:43:44 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 07/15  train_loss=0.26286  test_loss=0.33316  test_cos=0.6668  lr=1.00e-03
00:43:57 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 08/15  train_loss=0.26268  test_loss=0.33000  test_cos=0.6700  lr=1.00e-03
00:44:10 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 09/15  train_loss=0.26252  test_loss=0.32727  test_cos=0.6727  lr=1.00e-03
00:44:23 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 10/15  train_loss=0.26237  test_loss=0.32492  test_cos=0.6751  lr=1.00e-03
00:44:37 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 11/15  train_loss=0.26223  test_loss=0.32288  test_cos=0.6771  lr=1.00e-03
00:44:50 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 12/15  train_loss=0.26209  test_loss=0.32110  test_cos=0.6789  lr=1.00e-03
00:45:03 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 13/15  train_loss=0.26196  test_loss=0.31952  test_cos=0.6805  lr=1.00e-03
00:45:17 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 14/15  train_loss=0.26182  test_loss=0.31812  test_cos=0.6819  lr=1.00e-03
00:45:30 [INFO] [pplx-embed-1_to_nemotron-1b-free][deep] 15/15  train_loss=0.26169  test_loss=0.31687  test_cos=0.6831  lr=1.00e-03
00:45:30 [INFO] [pplx-embed-1_to_nemotron-1b-free] winner=linear best_epoch=15 best_test_cos=0.7025 saved → pplx-embed-1_to_nemotron-1b-free.pt  (418.9s)
00:45:30 [INFO]
─── [37/49] pplx-embed-1 → fastembed-bge-small ───
00:45:30 [INFO] [pplx-embed-1_to_fastembed-bge-small] 1024d → 384d
00:45:36 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 01/15  train_loss=0.08143  test_loss=0.13413  test_cos=0.8659  lr=1.00e-03
00:45:41 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 02/15  train_loss=0.07501  test_loss=0.12129  test_cos=0.8787  lr=1.00e-03
00:45:46 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 03/15  train_loss=0.07425  test_loss=0.11581  test_cos=0.8842  lr=1.00e-03
00:45:52 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 04/15  train_loss=0.07400  test_loss=0.11172  test_cos=0.8883  lr=1.00e-03
00:45:57 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 05/15  train_loss=0.07388  test_loss=0.10848  test_cos=0.8915  lr=1.00e-03
00:46:02 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 06/15  train_loss=0.07381  test_loss=0.10591  test_cos=0.8941  lr=1.00e-03
00:46:08 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 07/15  train_loss=0.07378  test_loss=0.10384  test_cos=0.8962  lr=1.00e-03
00:46:13 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 08/15  train_loss=0.07376  test_loss=0.10215  test_cos=0.8979  lr=1.00e-03
00:46:18 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 09/15  train_loss=0.07375  test_loss=0.10075  test_cos=0.8993  lr=1.00e-03
00:46:24 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 10/15  train_loss=0.07374  test_loss=0.09957  test_cos=0.9004  lr=1.00e-03
00:46:29 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 11/15  train_loss=0.07374  test_loss=0.09856  test_cos=0.9014  lr=1.00e-03
00:46:34 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 12/15  train_loss=0.07374  test_loss=0.09769  test_cos=0.9023  lr=1.00e-03
00:46:40 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 13/15  train_loss=0.07374  test_loss=0.09692  test_cos=0.9031  lr=1.00e-03
00:46:45 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 14/15  train_loss=0.07374  test_loss=0.09623  test_cos=0.9038  lr=1.00e-03
00:46:51 [INFO] [pplx-embed-1_to_fastembed-bge-small][linear] 15/15  train_loss=0.07374  test_loss=0.09562  test_cos=0.9044  lr=1.00e-03
00:46:56 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 01/15  train_loss=0.09557  test_loss=0.14811  test_cos=0.8519  lr=1.00e-03
00:47:01 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 02/15  train_loss=0.08093  test_loss=0.13427  test_cos=0.8657  lr=1.00e-03
00:47:06 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 03/15  train_loss=0.07997  test_loss=0.12889  test_cos=0.8711  lr=1.00e-03
00:47:11 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 04/15  train_loss=0.07962  test_loss=0.12515  test_cos=0.8749  lr=1.00e-03
00:47:16 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 05/15  train_loss=0.07943  test_loss=0.12245  test_cos=0.8775  lr=1.00e-03
00:47:21 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 06/15  train_loss=0.07930  test_loss=0.12041  test_cos=0.8796  lr=1.00e-03
00:47:26 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 07/15  train_loss=0.07921  test_loss=0.11876  test_cos=0.8812  lr=1.00e-03
00:47:31 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 08/15  train_loss=0.07912  test_loss=0.11739  test_cos=0.8826  lr=1.00e-03
00:47:36 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 09/15  train_loss=0.07905  test_loss=0.11623  test_cos=0.8838  lr=1.00e-03
00:47:41 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 10/15  train_loss=0.07898  test_loss=0.11525  test_cos=0.8848  lr=1.00e-03
00:47:46 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 11/15  train_loss=0.07892  test_loss=0.11441  test_cos=0.8856  lr=1.00e-03
00:47:51 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 12/15  train_loss=0.07886  test_loss=0.11370  test_cos=0.8863  lr=1.00e-03
00:47:56 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 13/15  train_loss=0.07880  test_loss=0.11309  test_cos=0.8869  lr=1.00e-03
00:48:00 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 14/15  train_loss=0.07874  test_loss=0.11256  test_cos=0.8874  lr=1.00e-03
00:48:05 [INFO] [pplx-embed-1_to_fastembed-bge-small][deep] 15/15  train_loss=0.07868  test_loss=0.11211  test_cos=0.8879  lr=1.00e-03
00:48:05 [INFO] [pplx-embed-1_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.9044 saved → pplx-embed-1_to_fastembed-bge-small.pt  (155.3s)
00:48:05 [INFO]
─── [38/49] nemotron-1b-free → te3-small ───
00:48:05 [INFO] [nemotron-1b-free_to_te3-small] 2048d → 1536d
00:48:24 [INFO] [nemotron-1b-free_to_te3-small][linear] 01/15  train_loss=0.14152  test_loss=0.19386  test_cos=0.8061  lr=1.00e-03
00:48:43 [INFO] [nemotron-1b-free_to_te3-small][linear] 02/15  train_loss=0.12820  test_loss=0.17779  test_cos=0.8222  lr=1.00e-03
00:49:02 [INFO] [nemotron-1b-free_to_te3-small][linear] 03/15  train_loss=0.12614  test_loss=0.17029  test_cos=0.8297  lr=1.00e-03
00:49:21 [INFO] [nemotron-1b-free_to_te3-small][linear] 04/15  train_loss=0.12508  test_loss=0.16521  test_cos=0.8348  lr=1.00e-03
00:49:40 [INFO] [nemotron-1b-free_to_te3-small][linear] 05/15  train_loss=0.12440  test_loss=0.16142  test_cos=0.8386  lr=1.00e-03
00:49:59 [INFO] [nemotron-1b-free_to_te3-small][linear] 06/15  train_loss=0.12392  test_loss=0.15843  test_cos=0.8416  lr=1.00e-03
00:50:18 [INFO] [nemotron-1b-free_to_te3-small][linear] 07/15  train_loss=0.12356  test_loss=0.15601  test_cos=0.8440  lr=1.00e-03
00:50:37 [INFO] [nemotron-1b-free_to_te3-small][linear] 08/15  train_loss=0.12328  test_loss=0.15399  test_cos=0.8460  lr=1.00e-03
00:50:56 [INFO] [nemotron-1b-free_to_te3-small][linear] 09/15  train_loss=0.12305  test_loss=0.15227  test_cos=0.8477  lr=1.00e-03
00:51:15 [INFO] [nemotron-1b-free_to_te3-small][linear] 10/15  train_loss=0.12287  test_loss=0.15078  test_cos=0.8492  lr=1.00e-03
00:51:34 [INFO] [nemotron-1b-free_to_te3-small][linear] 11/15  train_loss=0.12271  test_loss=0.14948  test_cos=0.8505  lr=1.00e-03
00:51:53 [INFO] [nemotron-1b-free_to_te3-small][linear] 12/15  train_loss=0.12259  test_loss=0.14833  test_cos=0.8517  lr=1.00e-03
00:52:12 [INFO] [nemotron-1b-free_to_te3-small][linear] 13/15  train_loss=0.12247  test_loss=0.14730  test_cos=0.8527  lr=1.00e-03
00:52:31 [INFO] [nemotron-1b-free_to_te3-small][linear] 14/15  train_loss=0.12238  test_loss=0.14637  test_cos=0.8536  lr=1.00e-03
00:52:50 [INFO] [nemotron-1b-free_to_te3-small][linear] 15/15  train_loss=0.12229  test_loss=0.14553  test_cos=0.8545  lr=1.00e-03
00:53:07 [INFO] [nemotron-1b-free_to_te3-small][deep] 01/15  train_loss=0.15845  test_loss=0.22419  test_cos=0.7758  lr=1.00e-03
00:53:25 [INFO] [nemotron-1b-free_to_te3-small][deep] 02/15  train_loss=0.13310  test_loss=0.19930  test_cos=0.8007  lr=1.00e-03
00:53:42 [INFO] [nemotron-1b-free_to_te3-small][deep] 03/15  train_loss=0.12964  test_loss=0.18766  test_cos=0.8123  lr=1.00e-03
00:54:00 [INFO] [nemotron-1b-free_to_te3-small][deep] 04/15  train_loss=0.12781  test_loss=0.18041  test_cos=0.8196  lr=1.00e-03
00:54:17 [INFO] [nemotron-1b-free_to_te3-small][deep] 05/15  train_loss=0.12654  test_loss=0.17532  test_cos=0.8247  lr=1.00e-03
00:54:34 [INFO] [nemotron-1b-free_to_te3-small][deep] 06/15  train_loss=0.12555  test_loss=0.17136  test_cos=0.8286  lr=1.00e-03
00:54:52 [INFO] [nemotron-1b-free_to_te3-small][deep] 07/15  train_loss=0.12471  test_loss=0.16798  test_cos=0.8320  lr=1.00e-03
00:55:09 [INFO] [nemotron-1b-free_to_te3-small][deep] 08/15  train_loss=0.12397  test_loss=0.16500  test_cos=0.8350  lr=1.00e-03
00:55:27 [INFO] [nemotron-1b-free_to_te3-small][deep] 09/15  train_loss=0.12331  test_loss=0.16235  test_cos=0.8377  lr=1.00e-03
00:55:45 [INFO] [nemotron-1b-free_to_te3-small][deep] 10/15  train_loss=0.12270  test_loss=0.15996  test_cos=0.8400  lr=1.00e-03
00:56:02 [INFO] [nemotron-1b-free_to_te3-small][deep] 11/15  train_loss=0.12213  test_loss=0.15779  test_cos=0.8422  lr=1.00e-03
00:56:20 [INFO] [nemotron-1b-free_to_te3-small][deep] 12/15  train_loss=0.12159  test_loss=0.15582  test_cos=0.8442  lr=1.00e-03
00:56:37 [INFO] [nemotron-1b-free_to_te3-small][deep] 13/15  train_loss=0.12107  test_loss=0.15403  test_cos=0.8460  lr=1.00e-03
00:56:55 [INFO] [nemotron-1b-free_to_te3-small][deep] 14/15  train_loss=0.12057  test_loss=0.15239  test_cos=0.8476  lr=1.00e-03
00:57:12 [INFO] [nemotron-1b-free_to_te3-small][deep] 15/15  train_loss=0.12009  test_loss=0.15087  test_cos=0.8491  lr=1.00e-03
00:57:12 [INFO] [nemotron-1b-free_to_te3-small] winner=linear best_epoch=15 best_test_cos=0.8545 saved → nemotron-1b-free_to_te3-small.pt  (546.9s)
00:57:12 [INFO]
─── [39/49] nemotron-1b-free → qwen3-emb-8b ───
00:57:12 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] 2048d → 4096d
00:58:02 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 01/15  train_loss=0.14453  test_loss=0.21851  test_cos=0.7815  lr=1.00e-03
00:58:54 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 02/15  train_loss=0.13106  test_loss=0.19915  test_cos=0.8008  lr=1.00e-03
00:59:45 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 03/15  train_loss=0.12893  test_loss=0.18981  test_cos=0.8102  lr=1.00e-03
01:00:36 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 04/15  train_loss=0.12788  test_loss=0.18337  test_cos=0.8166  lr=1.00e-03
01:01:27 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 05/15  train_loss=0.12721  test_loss=0.17849  test_cos=0.8215  lr=1.00e-03
01:02:19 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 06/15  train_loss=0.12675  test_loss=0.17464  test_cos=0.8254  lr=1.00e-03
01:03:10 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 07/15  train_loss=0.12641  test_loss=0.17151  test_cos=0.8285  lr=1.00e-03
01:04:02 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 08/15  train_loss=0.12614  test_loss=0.16889  test_cos=0.8311  lr=1.00e-03
01:04:54 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 09/15  train_loss=0.12593  test_loss=0.16667  test_cos=0.8333  lr=1.00e-03
01:05:46 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 10/15  train_loss=0.12577  test_loss=0.16474  test_cos=0.8353  lr=1.00e-03
01:06:38 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 11/15  train_loss=0.12563  test_loss=0.16304  test_cos=0.8370  lr=1.00e-03
01:07:31 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 12/15  train_loss=0.12551  test_loss=0.16153  test_cos=0.8385  lr=1.00e-03
01:08:23 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 13/15  train_loss=0.12541  test_loss=0.16018  test_cos=0.8398  lr=1.00e-03
01:09:15 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 14/15  train_loss=0.12533  test_loss=0.15896  test_cos=0.8410  lr=1.00e-03
01:10:08 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][linear] 15/15  train_loss=0.12526  test_loss=0.15785  test_cos=0.8422  lr=1.00e-03
01:10:52 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 01/15  train_loss=0.16489  test_loss=0.25327  test_cos=0.7467  lr=1.00e-03
01:11:36 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 02/15  train_loss=0.13642  test_loss=0.22439  test_cos=0.7756  lr=1.00e-03
01:12:19 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 03/15  train_loss=0.13246  test_loss=0.21095  test_cos=0.7891  lr=1.00e-03
01:13:03 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 04/15  train_loss=0.13027  test_loss=0.20271  test_cos=0.7973  lr=1.00e-03
01:13:47 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 05/15  train_loss=0.12868  test_loss=0.19598  test_cos=0.8040  lr=1.00e-03
01:14:31 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 06/15  train_loss=0.12743  test_loss=0.19056  test_cos=0.8094  lr=1.00e-03
01:15:15 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 07/15  train_loss=0.12636  test_loss=0.18606  test_cos=0.8139  lr=1.00e-03
01:15:59 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 08/15  train_loss=0.12542  test_loss=0.18182  test_cos=0.8182  lr=1.00e-03
01:16:43 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 09/15  train_loss=0.12457  test_loss=0.17792  test_cos=0.8221  lr=1.00e-03
01:17:27 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 10/15  train_loss=0.12378  test_loss=0.17437  test_cos=0.8256  lr=1.00e-03
01:18:11 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 11/15  train_loss=0.12304  test_loss=0.17112  test_cos=0.8289  lr=1.00e-03
01:18:55 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 12/15  train_loss=0.12235  test_loss=0.16814  test_cos=0.8319  lr=1.00e-03
01:19:40 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 13/15  train_loss=0.12169  test_loss=0.16539  test_cos=0.8346  lr=1.00e-03
01:20:24 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 14/15  train_loss=0.12105  test_loss=0.16285  test_cos=0.8372  lr=1.00e-03
01:21:08 [INFO] [nemotron-1b-free_to_qwen3-emb-8b][deep] 15/15  train_loss=0.12044  test_loss=0.16049  test_cos=0.8395  lr=1.00e-03
01:21:08 [INFO] [nemotron-1b-free_to_qwen3-emb-8b] winner=linear best_epoch=15 best_test_cos=0.8422 saved → nemotron-1b-free_to_qwen3-emb-8b.pt  (1435.5s)
01:21:08 [INFO]
─── [40/49] nemotron-1b-free → bge-m3 ───
01:21:08 [INFO] [nemotron-1b-free_to_bge-m3] 2048d → 1024d
01:21:24 [INFO] [nemotron-1b-free_to_bge-m3][linear] 01/15  train_loss=0.12357  test_loss=0.15481  test_cos=0.8452  lr=1.00e-03
01:21:39 [INFO] [nemotron-1b-free_to_bge-m3][linear] 02/15  train_loss=0.11329  test_loss=0.14526  test_cos=0.8547  lr=1.00e-03
01:21:55 [INFO] [nemotron-1b-free_to_bge-m3][linear] 03/15  train_loss=0.11174  test_loss=0.14048  test_cos=0.8595  lr=1.00e-03
01:22:10 [INFO] [nemotron-1b-free_to_bge-m3][linear] 04/15  train_loss=0.11093  test_loss=0.13717  test_cos=0.8628  lr=1.00e-03
01:22:26 [INFO] [nemotron-1b-free_to_bge-m3][linear] 05/15  train_loss=0.11040  test_loss=0.13467  test_cos=0.8653  lr=1.00e-03
01:22:42 [INFO] [nemotron-1b-free_to_bge-m3][linear] 06/15  train_loss=0.11002  test_loss=0.13269  test_cos=0.8673  lr=1.00e-03
01:22:57 [INFO] [nemotron-1b-free_to_bge-m3][linear] 07/15  train_loss=0.10974  test_loss=0.13107  test_cos=0.8689  lr=1.00e-03
01:23:13 [INFO] [nemotron-1b-free_to_bge-m3][linear] 08/15  train_loss=0.10952  test_loss=0.12972  test_cos=0.8703  lr=1.00e-03
01:23:28 [INFO] [nemotron-1b-free_to_bge-m3][linear] 09/15  train_loss=0.10934  test_loss=0.12857  test_cos=0.8714  lr=1.00e-03
01:23:43 [INFO] [nemotron-1b-free_to_bge-m3][linear] 10/15  train_loss=0.10919  test_loss=0.12758  test_cos=0.8724  lr=1.00e-03
01:23:59 [INFO] [nemotron-1b-free_to_bge-m3][linear] 11/15  train_loss=0.10907  test_loss=0.12670  test_cos=0.8733  lr=1.00e-03
01:24:14 [INFO] [nemotron-1b-free_to_bge-m3][linear] 12/15  train_loss=0.10897  test_loss=0.12593  test_cos=0.8741  lr=1.00e-03
01:24:30 [INFO] [nemotron-1b-free_to_bge-m3][linear] 13/15  train_loss=0.10888  test_loss=0.12524  test_cos=0.8748  lr=1.00e-03
01:24:45 [INFO] [nemotron-1b-free_to_bge-m3][linear] 14/15  train_loss=0.10880  test_loss=0.12462  test_cos=0.8754  lr=1.00e-03
01:25:01 [INFO] [nemotron-1b-free_to_bge-m3][linear] 15/15  train_loss=0.10873  test_loss=0.12405  test_cos=0.8759  lr=1.00e-03
01:25:14 [INFO] [nemotron-1b-free_to_bge-m3][deep] 01/15  train_loss=0.13409  test_loss=0.17081  test_cos=0.8292  lr=1.00e-03
01:25:27 [INFO] [nemotron-1b-free_to_bge-m3][deep] 02/15  train_loss=0.11573  test_loss=0.15679  test_cos=0.8432  lr=1.00e-03
01:25:41 [INFO] [nemotron-1b-free_to_bge-m3][deep] 03/15  train_loss=0.11361  test_loss=0.15075  test_cos=0.8493  lr=1.00e-03
01:25:54 [INFO] [nemotron-1b-free_to_bge-m3][deep] 04/15  train_loss=0.11252  test_loss=0.14678  test_cos=0.8532  lr=1.00e-03
01:26:07 [INFO] [nemotron-1b-free_to_bge-m3][deep] 05/15  train_loss=0.11181  test_loss=0.14390  test_cos=0.8561  lr=1.00e-03
01:26:20 [INFO] [nemotron-1b-free_to_bge-m3][deep] 06/15  train_loss=0.11130  test_loss=0.14166  test_cos=0.8583  lr=1.00e-03
01:26:34 [INFO] [nemotron-1b-free_to_bge-m3][deep] 07/15  train_loss=0.11091  test_loss=0.13982  test_cos=0.8602  lr=1.00e-03
01:26:47 [INFO] [nemotron-1b-free_to_bge-m3][deep] 08/15  train_loss=0.11060  test_loss=0.13824  test_cos=0.8618  lr=1.00e-03
01:27:00 [INFO] [nemotron-1b-free_to_bge-m3][deep] 09/15  train_loss=0.11033  test_loss=0.13685  test_cos=0.8632  lr=1.00e-03
01:27:13 [INFO] [nemotron-1b-free_to_bge-m3][deep] 10/15  train_loss=0.11009  test_loss=0.13566  test_cos=0.8643  lr=1.00e-03
01:27:27 [INFO] [nemotron-1b-free_to_bge-m3][deep] 11/15  train_loss=0.10987  test_loss=0.13463  test_cos=0.8654  lr=1.00e-03
01:27:40 [INFO] [nemotron-1b-free_to_bge-m3][deep] 12/15  train_loss=0.10968  test_loss=0.13370  test_cos=0.8663  lr=1.00e-03
01:27:53 [INFO] [nemotron-1b-free_to_bge-m3][deep] 13/15  train_loss=0.10949  test_loss=0.13283  test_cos=0.8672  lr=1.00e-03
01:28:06 [INFO] [nemotron-1b-free_to_bge-m3][deep] 14/15  train_loss=0.10931  test_loss=0.13202  test_cos=0.8680  lr=1.00e-03
01:28:20 [INFO] [nemotron-1b-free_to_bge-m3][deep] 15/15  train_loss=0.10914  test_loss=0.13126  test_cos=0.8687  lr=1.00e-03
01:28:20 [INFO] [nemotron-1b-free_to_bge-m3] winner=linear best_epoch=15 best_test_cos=0.8759 saved → nemotron-1b-free_to_bge-m3.pt  (431.8s)
01:28:20 [INFO]
─── [41/49] nemotron-1b-free → me5-large ───
01:28:20 [INFO] [nemotron-1b-free_to_me5-large] 2048d → 1024d
01:28:35 [INFO] [nemotron-1b-free_to_me5-large][linear] 01/15  train_loss=0.04942  test_loss=0.06407  test_cos=0.9359  lr=1.00e-03
01:28:51 [INFO] [nemotron-1b-free_to_me5-large][linear] 02/15  train_loss=0.04424  test_loss=0.06017  test_cos=0.9398  lr=1.00e-03
01:29:06 [INFO] [nemotron-1b-free_to_me5-large][linear] 03/15  train_loss=0.04359  test_loss=0.05813  test_cos=0.9419  lr=1.00e-03
01:29:22 [INFO] [nemotron-1b-free_to_me5-large][linear] 04/15  train_loss=0.04325  test_loss=0.05659  test_cos=0.9434  lr=1.00e-03
01:29:37 [INFO] [nemotron-1b-free_to_me5-large][linear] 05/15  train_loss=0.04303  test_loss=0.05538  test_cos=0.9446  lr=1.00e-03
01:29:53 [INFO] [nemotron-1b-free_to_me5-large][linear] 06/15  train_loss=0.04287  test_loss=0.05441  test_cos=0.9456  lr=1.00e-03
01:30:09 [INFO] [nemotron-1b-free_to_me5-large][linear] 07/15  train_loss=0.04276  test_loss=0.05363  test_cos=0.9464  lr=1.00e-03
01:30:24 [INFO] [nemotron-1b-free_to_me5-large][linear] 08/15  train_loss=0.04266  test_loss=0.05299  test_cos=0.9470  lr=1.00e-03
01:30:40 [INFO] [nemotron-1b-free_to_me5-large][linear] 09/15  train_loss=0.04259  test_loss=0.05245  test_cos=0.9475  lr=1.00e-03
01:30:55 [INFO] [nemotron-1b-free_to_me5-large][linear] 10/15  train_loss=0.04253  test_loss=0.05200  test_cos=0.9480  lr=1.00e-03
01:31:11 [INFO] [nemotron-1b-free_to_me5-large][linear] 11/15  train_loss=0.04248  test_loss=0.05160  test_cos=0.9484  lr=1.00e-03
01:31:26 [INFO] [nemotron-1b-free_to_me5-large][linear] 12/15  train_loss=0.04244  test_loss=0.05125  test_cos=0.9488  lr=1.00e-03
01:31:42 [INFO] [nemotron-1b-free_to_me5-large][linear] 13/15  train_loss=0.04241  test_loss=0.05094  test_cos=0.9491  lr=1.00e-03
01:31:57 [INFO] [nemotron-1b-free_to_me5-large][linear] 14/15  train_loss=0.04237  test_loss=0.05065  test_cos=0.9493  lr=1.00e-03
01:32:13 [INFO] [nemotron-1b-free_to_me5-large][linear] 15/15  train_loss=0.04235  test_loss=0.05039  test_cos=0.9496  lr=1.00e-03
01:32:26 [INFO] [nemotron-1b-free_to_me5-large][deep] 01/15  train_loss=0.05585  test_loss=0.07444  test_cos=0.9256  lr=1.00e-03
01:32:39 [INFO] [nemotron-1b-free_to_me5-large][deep] 02/15  train_loss=0.04553  test_loss=0.06856  test_cos=0.9314  lr=1.00e-03
01:32:53 [INFO] [nemotron-1b-free_to_me5-large][deep] 03/15  train_loss=0.04456  test_loss=0.06555  test_cos=0.9345  lr=1.00e-03
01:33:06 [INFO] [nemotron-1b-free_to_me5-large][deep] 04/15  train_loss=0.04410  test_loss=0.06332  test_cos=0.9367  lr=1.00e-03
01:33:19 [INFO] [nemotron-1b-free_to_me5-large][deep] 05/15  train_loss=0.04382  test_loss=0.06156  test_cos=0.9384  lr=1.00e-03
01:33:33 [INFO] [nemotron-1b-free_to_me5-large][deep] 06/15  train_loss=0.04362  test_loss=0.06017  test_cos=0.9398  lr=1.00e-03
01:33:46 [INFO] [nemotron-1b-free_to_me5-large][deep] 07/15  train_loss=0.04346  test_loss=0.05913  test_cos=0.9409  lr=1.00e-03
01:33:59 [INFO] [nemotron-1b-free_to_me5-large][deep] 08/15  train_loss=0.04334  test_loss=0.05829  test_cos=0.9417  lr=1.00e-03
01:34:13 [INFO] [nemotron-1b-free_to_me5-large][deep] 09/15  train_loss=0.04323  test_loss=0.05758  test_cos=0.9424  lr=1.00e-03
01:34:26 [INFO] [nemotron-1b-free_to_me5-large][deep] 10/15  train_loss=0.04314  test_loss=0.05697  test_cos=0.9430  lr=1.00e-03
01:34:39 [INFO] [nemotron-1b-free_to_me5-large][deep] 11/15  train_loss=0.04307  test_loss=0.05644  test_cos=0.9436  lr=1.00e-03
01:34:52 [INFO] [nemotron-1b-free_to_me5-large][deep] 12/15  train_loss=0.04300  test_loss=0.05598  test_cos=0.9440  lr=1.00e-03
01:35:05 [INFO] [nemotron-1b-free_to_me5-large][deep] 13/15  train_loss=0.04294  test_loss=0.05557  test_cos=0.9444  lr=1.00e-03
01:35:19 [INFO] [nemotron-1b-free_to_me5-large][deep] 14/15  train_loss=0.04288  test_loss=0.05520  test_cos=0.9448  lr=1.00e-03
01:35:32 [INFO] [nemotron-1b-free_to_me5-large][deep] 15/15  train_loss=0.04283  test_loss=0.05488  test_cos=0.9451  lr=1.00e-03
01:35:32 [INFO] [nemotron-1b-free_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9496 saved → nemotron-1b-free_to_me5-large.pt  (432.3s)
01:35:32 [INFO]
─── [42/49] nemotron-1b-free → pplx-embed-1 ───
01:35:32 [INFO] [nemotron-1b-free_to_pplx-embed-1] 2048d → 1024d
01:35:47 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 01/15  train_loss=0.20121  test_loss=0.27914  test_cos=0.7209  lr=1.00e-03
01:36:03 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 02/15  train_loss=0.18683  test_loss=0.25787  test_cos=0.7421  lr=1.00e-03
01:36:18 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 03/15  train_loss=0.18413  test_loss=0.24747  test_cos=0.7525  lr=1.00e-03
01:36:34 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 04/15  train_loss=0.18274  test_loss=0.24028  test_cos=0.7597  lr=1.00e-03
01:36:49 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 05/15  train_loss=0.18184  test_loss=0.23481  test_cos=0.7652  lr=1.00e-03
01:37:04 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 06/15  train_loss=0.18121  test_loss=0.23047  test_cos=0.7695  lr=1.00e-03
01:37:20 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 07/15  train_loss=0.18073  test_loss=0.22693  test_cos=0.7731  lr=1.00e-03
01:37:35 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 08/15  train_loss=0.18036  test_loss=0.22399  test_cos=0.7760  lr=1.00e-03
01:37:51 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 09/15  train_loss=0.18006  test_loss=0.22151  test_cos=0.7785  lr=1.00e-03
01:38:06 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 10/15  train_loss=0.17982  test_loss=0.21937  test_cos=0.7806  lr=1.00e-03
01:38:21 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 11/15  train_loss=0.17962  test_loss=0.21751  test_cos=0.7825  lr=1.00e-03
01:38:37 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 12/15  train_loss=0.17945  test_loss=0.21587  test_cos=0.7841  lr=1.00e-03
01:38:52 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 13/15  train_loss=0.17930  test_loss=0.21441  test_cos=0.7856  lr=1.00e-03
01:39:08 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 14/15  train_loss=0.17917  test_loss=0.21310  test_cos=0.7869  lr=1.00e-03
01:39:23 [INFO] [nemotron-1b-free_to_pplx-embed-1][linear] 15/15  train_loss=0.17906  test_loss=0.21191  test_cos=0.7881  lr=1.00e-03
01:39:37 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 01/15  train_loss=0.22394  test_loss=0.31426  test_cos=0.6857  lr=1.00e-03
01:39:50 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 02/15  train_loss=0.19577  test_loss=0.28594  test_cos=0.7141  lr=1.00e-03
01:40:03 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 03/15  train_loss=0.19220  test_loss=0.27298  test_cos=0.7270  lr=1.00e-03
01:40:16 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 04/15  train_loss=0.19044  test_loss=0.26459  test_cos=0.7354  lr=1.00e-03
01:40:29 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 05/15  train_loss=0.18928  test_loss=0.25830  test_cos=0.7417  lr=1.00e-03
01:40:42 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 06/15  train_loss=0.18839  test_loss=0.25328  test_cos=0.7467  lr=1.00e-03
01:40:54 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 07/15  train_loss=0.18764  test_loss=0.24902  test_cos=0.7510  lr=1.00e-03
01:41:07 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 08/15  train_loss=0.18699  test_loss=0.24530  test_cos=0.7547  lr=1.00e-03
01:41:20 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 09/15  train_loss=0.18640  test_loss=0.24209  test_cos=0.7579  lr=1.00e-03
01:41:32 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 10/15  train_loss=0.18588  test_loss=0.23929  test_cos=0.7607  lr=1.00e-03
01:41:45 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 11/15  train_loss=0.18539  test_loss=0.23683  test_cos=0.7632  lr=1.00e-03
01:41:58 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 12/15  train_loss=0.18494  test_loss=0.23462  test_cos=0.7654  lr=1.00e-03
01:42:10 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 13/15  train_loss=0.18450  test_loss=0.23260  test_cos=0.7674  lr=1.00e-03
01:42:23 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 14/15  train_loss=0.18409  test_loss=0.23075  test_cos=0.7692  lr=1.00e-03
01:42:36 [INFO] [nemotron-1b-free_to_pplx-embed-1][deep] 15/15  train_loss=0.18369  test_loss=0.22903  test_cos=0.7710  lr=1.00e-03
01:42:36 [INFO] [nemotron-1b-free_to_pplx-embed-1] winner=linear best_epoch=15 best_test_cos=0.7881 saved → nemotron-1b-free_to_pplx-embed-1.pt  (423.7s)
01:42:36 [INFO]
─── [43/49] nemotron-1b-free → fastembed-bge-small ───
01:42:36 [INFO] [nemotron-1b-free_to_fastembed-bge-small] 2048d → 384d
01:42:44 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 01/15  train_loss=0.07819  test_loss=0.11914  test_cos=0.8809  lr=1.00e-03
01:42:53 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 02/15  train_loss=0.07224  test_loss=0.10794  test_cos=0.8921  lr=1.00e-03
01:43:01 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 03/15  train_loss=0.07107  test_loss=0.10268  test_cos=0.8973  lr=1.00e-03
01:43:10 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 04/15  train_loss=0.07048  test_loss=0.09894  test_cos=0.9011  lr=1.00e-03
01:43:18 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 05/15  train_loss=0.07009  test_loss=0.09609  test_cos=0.9039  lr=1.00e-03
01:43:27 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 06/15  train_loss=0.06982  test_loss=0.09386  test_cos=0.9061  lr=1.00e-03
01:43:35 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 07/15  train_loss=0.06961  test_loss=0.09207  test_cos=0.9079  lr=1.00e-03
01:43:44 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 08/15  train_loss=0.06945  test_loss=0.09060  test_cos=0.9094  lr=1.00e-03
01:43:52 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 09/15  train_loss=0.06933  test_loss=0.08936  test_cos=0.9106  lr=1.00e-03
01:44:01 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 10/15  train_loss=0.06922  test_loss=0.08829  test_cos=0.9117  lr=1.00e-03
01:44:09 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 11/15  train_loss=0.06914  test_loss=0.08737  test_cos=0.9126  lr=1.00e-03
01:44:18 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 12/15  train_loss=0.06907  test_loss=0.08656  test_cos=0.9134  lr=1.00e-03
01:44:26 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 13/15  train_loss=0.06901  test_loss=0.08584  test_cos=0.9142  lr=1.00e-03
01:44:35 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 14/15  train_loss=0.06896  test_loss=0.08520  test_cos=0.9148  lr=1.00e-03
01:44:43 [INFO] [nemotron-1b-free_to_fastembed-bge-small][linear] 15/15  train_loss=0.06891  test_loss=0.08462  test_cos=0.9154  lr=1.00e-03
01:44:51 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 01/15  train_loss=0.09513  test_loss=0.14517  test_cos=0.8548  lr=1.00e-03
01:44:58 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 02/15  train_loss=0.08009  test_loss=0.12698  test_cos=0.8730  lr=1.00e-03
01:45:06 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 03/15  train_loss=0.07855  test_loss=0.12035  test_cos=0.8797  lr=1.00e-03
01:45:13 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 04/15  train_loss=0.07787  test_loss=0.11602  test_cos=0.8840  lr=1.00e-03
01:45:20 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 05/15  train_loss=0.07747  test_loss=0.11296  test_cos=0.8870  lr=1.00e-03
01:45:28 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 06/15  train_loss=0.07720  test_loss=0.11064  test_cos=0.8894  lr=1.00e-03
01:45:35 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 07/15  train_loss=0.07700  test_loss=0.10875  test_cos=0.8912  lr=1.00e-03
01:45:42 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 08/15  train_loss=0.07685  test_loss=0.10714  test_cos=0.8929  lr=1.00e-03
01:45:50 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 09/15  train_loss=0.07672  test_loss=0.10575  test_cos=0.8943  lr=1.00e-03
01:45:57 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 10/15  train_loss=0.07661  test_loss=0.10455  test_cos=0.8954  lr=1.00e-03
01:46:04 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 11/15  train_loss=0.07652  test_loss=0.10353  test_cos=0.8965  lr=1.00e-03
01:46:12 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 12/15  train_loss=0.07643  test_loss=0.10265  test_cos=0.8973  lr=1.00e-03
01:46:19 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 13/15  train_loss=0.07636  test_loss=0.10190  test_cos=0.8981  lr=1.00e-03
01:46:26 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 14/15  train_loss=0.07629  test_loss=0.10124  test_cos=0.8988  lr=1.00e-03
01:46:33 [INFO] [nemotron-1b-free_to_fastembed-bge-small][deep] 15/15  train_loss=0.07623  test_loss=0.10068  test_cos=0.8993  lr=1.00e-03
01:46:33 [INFO] [nemotron-1b-free_to_fastembed-bge-small] winner=linear best_epoch=15 best_test_cos=0.9154 saved → nemotron-1b-free_to_fastembed-bge-small.pt  (237.8s)
01:46:33 [INFO]
─── [44/49] fastembed-bge-small → te3-small ───
01:46:33 [INFO] [fastembed-bge-small_to_te3-small] 384d → 1536d
01:46:42 [INFO] [fastembed-bge-small_to_te3-small][linear] 01/15  train_loss=0.22546  test_loss=0.34578  test_cos=0.6542  lr=1.00e-03
01:46:50 [INFO] [fastembed-bge-small_to_te3-small][linear] 02/15  train_loss=0.21192  test_loss=0.33171  test_cos=0.6683  lr=1.00e-03
01:46:58 [INFO] [fastembed-bge-small_to_te3-small][linear] 03/15  train_loss=0.21147  test_loss=0.32493  test_cos=0.6751  lr=1.00e-03
01:47:06 [INFO] [fastembed-bge-small_to_te3-small][linear] 04/15  train_loss=0.21140  test_loss=0.31995  test_cos=0.6800  lr=1.00e-03
01:47:14 [INFO] [fastembed-bge-small_to_te3-small][linear] 05/15  train_loss=0.21141  test_loss=0.31583  test_cos=0.6842  lr=1.00e-03
01:47:23 [INFO] [fastembed-bge-small_to_te3-small][linear] 06/15  train_loss=0.21143  test_loss=0.31224  test_cos=0.6878  lr=1.00e-03
01:47:31 [INFO] [fastembed-bge-small_to_te3-small][linear] 07/15  train_loss=0.21147  test_loss=0.30901  test_cos=0.6910  lr=1.00e-03
01:47:39 [INFO] [fastembed-bge-small_to_te3-small][linear] 08/15  train_loss=0.21150  test_loss=0.30605  test_cos=0.6939  lr=1.00e-03
01:47:47 [INFO] [fastembed-bge-small_to_te3-small][linear] 09/15  train_loss=0.21153  test_loss=0.30331  test_cos=0.6967  lr=1.00e-03
01:47:56 [INFO] [fastembed-bge-small_to_te3-small][linear] 10/15  train_loss=0.21155  test_loss=0.30074  test_cos=0.6993  lr=1.00e-03
01:48:04 [INFO] [fastembed-bge-small_to_te3-small][linear] 11/15  train_loss=0.21158  test_loss=0.29833  test_cos=0.7017  lr=1.00e-03
01:48:12 [INFO] [fastembed-bge-small_to_te3-small][linear] 12/15  train_loss=0.21160  test_loss=0.29605  test_cos=0.7039  lr=1.00e-03
01:48:21 [INFO] [fastembed-bge-small_to_te3-small][linear] 13/15  train_loss=0.21163  test_loss=0.29390  test_cos=0.7061  lr=1.00e-03
01:48:29 [INFO] [fastembed-bge-small_to_te3-small][linear] 14/15  train_loss=0.21165  test_loss=0.29185  test_cos=0.7082  lr=1.00e-03
01:48:37 [INFO] [fastembed-bge-small_to_te3-small][linear] 15/15  train_loss=0.21166  test_loss=0.28991  test_cos=0.7101  lr=1.00e-03
01:48:45 [INFO] [fastembed-bge-small_to_te3-small][deep] 01/15  train_loss=0.25059  test_loss=0.34760  test_cos=0.6524  lr=1.00e-03
01:48:53 [INFO] [fastembed-bge-small_to_te3-small][deep] 02/15  train_loss=0.21996  test_loss=0.31967  test_cos=0.6803  lr=1.00e-03
01:49:00 [INFO] [fastembed-bge-small_to_te3-small][deep] 03/15  train_loss=0.21795  test_loss=0.30865  test_cos=0.6914  lr=1.00e-03
01:49:08 [INFO] [fastembed-bge-small_to_te3-small][deep] 04/15  train_loss=0.21752  test_loss=0.30346  test_cos=0.6965  lr=1.00e-03
01:49:16 [INFO] [fastembed-bge-small_to_te3-small][deep] 05/15  train_loss=0.21728  test_loss=0.30033  test_cos=0.6997  lr=1.00e-03
01:49:24 [INFO] [fastembed-bge-small_to_te3-small][deep] 06/15  train_loss=0.21713  test_loss=0.29773  test_cos=0.7023  lr=1.00e-03
01:49:31 [INFO] [fastembed-bge-small_to_te3-small][deep] 07/15  train_loss=0.21698  test_loss=0.29540  test_cos=0.7046  lr=1.00e-03
01:49:39 [INFO] [fastembed-bge-small_to_te3-small][deep] 08/15  train_loss=0.21684  test_loss=0.29320  test_cos=0.7068  lr=1.00e-03
01:49:47 [INFO] [fastembed-bge-small_to_te3-small][deep] 09/15  train_loss=0.21669  test_loss=0.29113  test_cos=0.7089  lr=1.00e-03
01:49:54 [INFO] [fastembed-bge-small_to_te3-small][deep] 10/15  train_loss=0.21652  test_loss=0.28915  test_cos=0.7109  lr=1.00e-03
01:50:02 [INFO] [fastembed-bge-small_to_te3-small][deep] 11/15  train_loss=0.21634  test_loss=0.28724  test_cos=0.7128  lr=1.00e-03
01:50:10 [INFO] [fastembed-bge-small_to_te3-small][deep] 12/15  train_loss=0.21614  test_loss=0.28540  test_cos=0.7146  lr=1.00e-03
01:50:17 [INFO] [fastembed-bge-small_to_te3-small][deep] 13/15  train_loss=0.21593  test_loss=0.28364  test_cos=0.7164  lr=1.00e-03
01:50:25 [INFO] [fastembed-bge-small_to_te3-small][deep] 14/15  train_loss=0.21570  test_loss=0.28194  test_cos=0.7181  lr=1.00e-03
01:50:32 [INFO] [fastembed-bge-small_to_te3-small][deep] 15/15  train_loss=0.21546  test_loss=0.28027  test_cos=0.7197  lr=1.00e-03
01:50:32 [INFO] [fastembed-bge-small_to_te3-small] winner=deep best_epoch=15 best_test_cos=0.7197 saved → fastembed-bge-small_to_te3-small.pt  (238.9s)
01:50:32 [INFO]
─── [45/49] fastembed-bge-small → qwen3-emb-8b ───
01:50:32 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] 384d → 4096d
01:50:51 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 01/15  train_loss=0.23893  test_loss=0.36562  test_cos=0.6344  lr=1.00e-03
01:51:10 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 02/15  train_loss=0.22494  test_loss=0.34840  test_cos=0.6516  lr=1.00e-03
01:51:29 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 03/15  train_loss=0.22440  test_loss=0.33928  test_cos=0.6607  lr=1.00e-03
01:51:49 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 04/15  train_loss=0.22434  test_loss=0.33279  test_cos=0.6672  lr=1.00e-03
01:52:08 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 05/15  train_loss=0.22436  test_loss=0.32766  test_cos=0.6723  lr=1.00e-03
01:52:27 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 06/15  train_loss=0.22441  test_loss=0.32337  test_cos=0.6766  lr=1.00e-03
01:52:46 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 07/15  train_loss=0.22447  test_loss=0.31965  test_cos=0.6803  lr=1.00e-03
01:53:05 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 08/15  train_loss=0.22452  test_loss=0.31634  test_cos=0.6837  lr=1.00e-03
01:53:24 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 09/15  train_loss=0.22458  test_loss=0.31334  test_cos=0.6867  lr=1.00e-03
01:53:43 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 10/15  train_loss=0.22462  test_loss=0.31058  test_cos=0.6894  lr=1.00e-03
01:54:02 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 11/15  train_loss=0.22467  test_loss=0.30802  test_cos=0.6920  lr=1.00e-03
01:54:21 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 12/15  train_loss=0.22471  test_loss=0.30563  test_cos=0.6944  lr=1.00e-03
01:54:40 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 13/15  train_loss=0.22475  test_loss=0.30339  test_cos=0.6966  lr=1.00e-03
01:54:59 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 14/15  train_loss=0.22478  test_loss=0.30129  test_cos=0.6987  lr=1.00e-03
01:55:18 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][linear] 15/15  train_loss=0.22481  test_loss=0.29931  test_cos=0.7007  lr=1.00e-03
01:55:35 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 01/15  train_loss=0.27041  test_loss=0.37463  test_cos=0.6254  lr=1.00e-03
01:55:52 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 02/15  train_loss=0.23478  test_loss=0.34884  test_cos=0.6512  lr=1.00e-03
01:56:08 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 03/15  train_loss=0.23256  test_loss=0.33567  test_cos=0.6643  lr=1.00e-03
01:56:25 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 04/15  train_loss=0.23202  test_loss=0.33010  test_cos=0.6699  lr=1.00e-03
01:56:41 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 05/15  train_loss=0.23171  test_loss=0.32713  test_cos=0.6729  lr=1.00e-03
01:56:58 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 06/15  train_loss=0.23145  test_loss=0.32459  test_cos=0.6754  lr=1.00e-03
01:57:15 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 07/15  train_loss=0.23118  test_loss=0.32179  test_cos=0.6782  lr=1.00e-03
01:57:32 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 08/15  train_loss=0.23091  test_loss=0.31908  test_cos=0.6809  lr=1.00e-03
01:57:50 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 09/15  train_loss=0.23063  test_loss=0.31665  test_cos=0.6833  lr=1.00e-03
01:58:07 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 10/15  train_loss=0.23033  test_loss=0.31439  test_cos=0.6856  lr=1.00e-03
01:58:24 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 11/15  train_loss=0.23002  test_loss=0.31216  test_cos=0.6878  lr=1.00e-03
01:58:40 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 12/15  train_loss=0.22971  test_loss=0.30986  test_cos=0.6901  lr=1.00e-03
01:58:56 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 13/15  train_loss=0.22939  test_loss=0.30750  test_cos=0.6925  lr=1.00e-03
01:59:12 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 14/15  train_loss=0.22907  test_loss=0.30514  test_cos=0.6949  lr=1.00e-03
01:59:28 [INFO] [fastembed-bge-small_to_qwen3-emb-8b][deep] 15/15  train_loss=0.22875  test_loss=0.30282  test_cos=0.6972  lr=1.00e-03
01:59:28 [INFO] [fastembed-bge-small_to_qwen3-emb-8b] winner=linear best_epoch=15 best_test_cos=0.7007 saved → fastembed-bge-small_to_qwen3-emb-8b.pt  (535.7s)
01:59:28 [INFO]
─── [46/49] fastembed-bge-small → bge-m3 ───
01:59:28 [INFO] [fastembed-bge-small_to_bge-m3] 384d → 1024d
01:59:35 [INFO] [fastembed-bge-small_to_bge-m3][linear] 01/15  train_loss=0.18168  test_loss=0.23031  test_cos=0.7697  lr=1.00e-03
01:59:41 [INFO] [fastembed-bge-small_to_bge-m3][linear] 02/15  train_loss=0.16968  test_loss=0.22312  test_cos=0.7769  lr=1.00e-03
01:59:46 [INFO] [fastembed-bge-small_to_bge-m3][linear] 03/15  train_loss=0.16934  test_loss=0.21983  test_cos=0.7802  lr=1.00e-03
01:59:52 [INFO] [fastembed-bge-small_to_bge-m3][linear] 04/15  train_loss=0.16928  test_loss=0.21762  test_cos=0.7824  lr=1.00e-03
01:59:58 [INFO] [fastembed-bge-small_to_bge-m3][linear] 05/15  train_loss=0.16927  test_loss=0.21598  test_cos=0.7840  lr=1.00e-03
02:00:04 [INFO] [fastembed-bge-small_to_bge-m3][linear] 06/15  train_loss=0.16928  test_loss=0.21472  test_cos=0.7853  lr=1.00e-03
02:00:10 [INFO] [fastembed-bge-small_to_bge-m3][linear] 07/15  train_loss=0.16930  test_loss=0.21373  test_cos=0.7863  lr=1.00e-03
02:00:16 [INFO] [fastembed-bge-small_to_bge-m3][linear] 08/15  train_loss=0.16932  test_loss=0.21291  test_cos=0.7871  lr=1.00e-03
02:00:22 [INFO] [fastembed-bge-small_to_bge-m3][linear] 09/15  train_loss=0.16934  test_loss=0.21220  test_cos=0.7878  lr=1.00e-03
02:00:28 [INFO] [fastembed-bge-small_to_bge-m3][linear] 10/15  train_loss=0.16937  test_loss=0.21156  test_cos=0.7884  lr=1.00e-03
02:00:34 [INFO] [fastembed-bge-small_to_bge-m3][linear] 11/15  train_loss=0.16938  test_loss=0.21095  test_cos=0.7890  lr=1.00e-03
02:00:40 [INFO] [fastembed-bge-small_to_bge-m3][linear] 12/15  train_loss=0.16940  test_loss=0.21037  test_cos=0.7896  lr=1.00e-03
02:00:46 [INFO] [fastembed-bge-small_to_bge-m3][linear] 13/15  train_loss=0.16942  test_loss=0.20981  test_cos=0.7902  lr=1.00e-03
02:00:52 [INFO] [fastembed-bge-small_to_bge-m3][linear] 14/15  train_loss=0.16943  test_loss=0.20925  test_cos=0.7907  lr=1.00e-03
02:00:58 [INFO] [fastembed-bge-small_to_bge-m3][linear] 15/15  train_loss=0.16945  test_loss=0.20870  test_cos=0.7913  lr=1.00e-03
02:01:04 [INFO] [fastembed-bge-small_to_bge-m3][deep] 01/15  train_loss=0.19750  test_loss=0.24630  test_cos=0.7537  lr=1.00e-03
02:01:10 [INFO] [fastembed-bge-small_to_bge-m3][deep] 02/15  train_loss=0.17370  test_loss=0.22969  test_cos=0.7703  lr=1.00e-03
02:01:15 [INFO] [fastembed-bge-small_to_bge-m3][deep] 03/15  train_loss=0.17235  test_loss=0.22395  test_cos=0.7760  lr=1.00e-03
02:01:21 [INFO] [fastembed-bge-small_to_bge-m3][deep] 04/15  train_loss=0.17209  test_loss=0.21971  test_cos=0.7803  lr=1.00e-03
02:01:27 [INFO] [fastembed-bge-small_to_bge-m3][deep] 05/15  train_loss=0.17200  test_loss=0.21667  test_cos=0.7833  lr=1.00e-03
02:01:33 [INFO] [fastembed-bge-small_to_bge-m3][deep] 06/15  train_loss=0.17196  test_loss=0.21456  test_cos=0.7854  lr=1.00e-03
02:01:38 [INFO] [fastembed-bge-small_to_bge-m3][deep] 07/15  train_loss=0.17192  test_loss=0.21295  test_cos=0.7871  lr=1.00e-03
02:01:44 [INFO] [fastembed-bge-small_to_bge-m3][deep] 08/15  train_loss=0.17189  test_loss=0.21167  test_cos=0.7883  lr=1.00e-03
02:01:50 [INFO] [fastembed-bge-small_to_bge-m3][deep] 09/15  train_loss=0.17185  test_loss=0.21063  test_cos=0.7894  lr=1.00e-03
02:01:56 [INFO] [fastembed-bge-small_to_bge-m3][deep] 10/15  train_loss=0.17181  test_loss=0.20977  test_cos=0.7902  lr=1.00e-03
02:02:01 [INFO] [fastembed-bge-small_to_bge-m3][deep] 11/15  train_loss=0.17176  test_loss=0.20900  test_cos=0.7910  lr=1.00e-03
02:02:07 [INFO] [fastembed-bge-small_to_bge-m3][deep] 12/15  train_loss=0.17171  test_loss=0.20828  test_cos=0.7917  lr=1.00e-03
02:02:13 [INFO] [fastembed-bge-small_to_bge-m3][deep] 13/15  train_loss=0.17164  test_loss=0.20761  test_cos=0.7924  lr=1.00e-03
02:02:19 [INFO] [fastembed-bge-small_to_bge-m3][deep] 14/15  train_loss=0.17157  test_loss=0.20697  test_cos=0.7930  lr=1.00e-03
02:02:24 [INFO] [fastembed-bge-small_to_bge-m3][deep] 15/15  train_loss=0.17148  test_loss=0.20635  test_cos=0.7936  lr=1.00e-03
02:02:24 [INFO] [fastembed-bge-small_to_bge-m3] winner=deep best_epoch=15 best_test_cos=0.7936 saved → fastembed-bge-small_to_bge-m3.pt  (176.3s)
02:02:24 [INFO]
─── [47/49] fastembed-bge-small → me5-large ───
02:02:24 [INFO] [fastembed-bge-small_to_me5-large] 384d → 1024d
02:02:31 [INFO] [fastembed-bge-small_to_me5-large][linear] 01/15  train_loss=0.06933  test_loss=0.08810  test_cos=0.9119  lr=1.00e-03
02:02:37 [INFO] [fastembed-bge-small_to_me5-large][linear] 02/15  train_loss=0.06178  test_loss=0.08548  test_cos=0.9145  lr=1.00e-03
02:02:43 [INFO] [fastembed-bge-small_to_me5-large][linear] 03/15  train_loss=0.06155  test_loss=0.08383  test_cos=0.9162  lr=1.00e-03
02:02:49 [INFO] [fastembed-bge-small_to_me5-large][linear] 04/15  train_loss=0.06150  test_loss=0.08272  test_cos=0.9173  lr=1.00e-03
02:02:54 [INFO] [fastembed-bge-small_to_me5-large][linear] 05/15  train_loss=0.06149  test_loss=0.08198  test_cos=0.9180  lr=1.00e-03
02:03:00 [INFO] [fastembed-bge-small_to_me5-large][linear] 06/15  train_loss=0.06149  test_loss=0.08148  test_cos=0.9185  lr=1.00e-03
02:03:07 [INFO] [fastembed-bge-small_to_me5-large][linear] 07/15  train_loss=0.06149  test_loss=0.08115  test_cos=0.9189  lr=1.00e-03
02:03:13 [INFO] [fastembed-bge-small_to_me5-large][linear] 08/15  train_loss=0.06150  test_loss=0.08093  test_cos=0.9191  lr=1.00e-03
02:03:18 [INFO] [fastembed-bge-small_to_me5-large][linear] 09/15  train_loss=0.06150  test_loss=0.08076  test_cos=0.9192  lr=1.00e-03
02:03:24 [INFO] [fastembed-bge-small_to_me5-large][linear] 10/15  train_loss=0.06151  test_loss=0.08063  test_cos=0.9194  lr=1.00e-03
02:03:30 [INFO] [fastembed-bge-small_to_me5-large][linear] 11/15  train_loss=0.06152  test_loss=0.08050  test_cos=0.9195  lr=1.00e-03
02:03:36 [INFO] [fastembed-bge-small_to_me5-large][linear] 12/15  train_loss=0.06152  test_loss=0.08038  test_cos=0.9196  lr=1.00e-03
02:03:42 [INFO] [fastembed-bge-small_to_me5-large][linear] 13/15  train_loss=0.06153  test_loss=0.08025  test_cos=0.9198  lr=1.00e-03
02:03:48 [INFO] [fastembed-bge-small_to_me5-large][linear] 14/15  train_loss=0.06153  test_loss=0.08010  test_cos=0.9199  lr=1.00e-03
02:03:54 [INFO] [fastembed-bge-small_to_me5-large][linear] 15/15  train_loss=0.06153  test_loss=0.07995  test_cos=0.9201  lr=1.00e-03
02:04:00 [INFO] [fastembed-bge-small_to_me5-large][deep] 01/15  train_loss=0.07768  test_loss=0.10008  test_cos=0.8999  lr=1.00e-03
02:04:06 [INFO] [fastembed-bge-small_to_me5-large][deep] 02/15  train_loss=0.06423  test_loss=0.09130  test_cos=0.9087  lr=1.00e-03
02:04:11 [INFO] [fastembed-bge-small_to_me5-large][deep] 03/15  train_loss=0.06330  test_loss=0.08750  test_cos=0.9125  lr=1.00e-03
02:04:17 [INFO] [fastembed-bge-small_to_me5-large][deep] 04/15  train_loss=0.06313  test_loss=0.08512  test_cos=0.9149  lr=1.00e-03
02:04:23 [INFO] [fastembed-bge-small_to_me5-large][deep] 05/15  train_loss=0.06310  test_loss=0.08356  test_cos=0.9164  lr=1.00e-03
02:04:28 [INFO] [fastembed-bge-small_to_me5-large][deep] 06/15  train_loss=0.06308  test_loss=0.08270  test_cos=0.9173  lr=1.00e-03
02:04:34 [INFO] [fastembed-bge-small_to_me5-large][deep] 07/15  train_loss=0.06308  test_loss=0.08220  test_cos=0.9178  lr=1.00e-03
02:04:40 [INFO] [fastembed-bge-small_to_me5-large][deep] 08/15  train_loss=0.06308  test_loss=0.08186  test_cos=0.9181  lr=1.00e-03
02:04:46 [INFO] [fastembed-bge-small_to_me5-large][deep] 09/15  train_loss=0.06308  test_loss=0.08158  test_cos=0.9184  lr=1.00e-03
02:04:51 [INFO] [fastembed-bge-small_to_me5-large][deep] 10/15  train_loss=0.06307  test_loss=0.08133  test_cos=0.9187  lr=1.00e-03
02:04:57 [INFO] [fastembed-bge-small_to_me5-large][deep] 11/15  train_loss=0.06307  test_loss=0.08109  test_cos=0.9189  lr=1.00e-03
02:05:03 [INFO] [fastembed-bge-small_to_me5-large][deep] 12/15  train_loss=0.06306  test_loss=0.08085  test_cos=0.9191  lr=1.00e-03
02:05:09 [INFO] [fastembed-bge-small_to_me5-large][deep] 13/15  train_loss=0.06305  test_loss=0.08061  test_cos=0.9194  lr=1.00e-03
02:05:14 [INFO] [fastembed-bge-small_to_me5-large][deep] 14/15  train_loss=0.06304  test_loss=0.08038  test_cos=0.9196  lr=1.00e-03
02:05:20 [INFO] [fastembed-bge-small_to_me5-large][deep] 15/15  train_loss=0.06303  test_loss=0.08014  test_cos=0.9199  lr=1.00e-03
02:05:20 [INFO] [fastembed-bge-small_to_me5-large] winner=linear best_epoch=15 best_test_cos=0.9201 saved → fastembed-bge-small_to_me5-large.pt  (175.6s)
02:05:20 [INFO]
─── [48/49] fastembed-bge-small → pplx-embed-1 ───
02:05:20 [INFO] [fastembed-bge-small_to_pplx-embed-1] 384d → 1024d
02:05:26 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 01/15  train_loss=0.29810  test_loss=0.43123  test_cos=0.5688  lr=1.00e-03
02:05:32 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 02/15  train_loss=0.28439  test_loss=0.41356  test_cos=0.5864  lr=1.00e-03
02:05:38 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 03/15  train_loss=0.28390  test_loss=0.40507  test_cos=0.5949  lr=1.00e-03
02:05:44 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 04/15  train_loss=0.28386  test_loss=0.39896  test_cos=0.6010  lr=1.00e-03
02:05:50 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 05/15  train_loss=0.28390  test_loss=0.39402  test_cos=0.6060  lr=1.00e-03
02:05:55 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 06/15  train_loss=0.28395  test_loss=0.38980  test_cos=0.6102  lr=1.00e-03
02:06:01 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 07/15  train_loss=0.28400  test_loss=0.38608  test_cos=0.6139  lr=1.00e-03
02:06:07 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 08/15  train_loss=0.28405  test_loss=0.38272  test_cos=0.6173  lr=1.00e-03
02:06:13 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 09/15  train_loss=0.28410  test_loss=0.37964  test_cos=0.6204  lr=1.00e-03
02:06:19 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 10/15  train_loss=0.28414  test_loss=0.37678  test_cos=0.6232  lr=1.00e-03
02:06:25 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 11/15  train_loss=0.28417  test_loss=0.37412  test_cos=0.6259  lr=1.00e-03
02:06:31 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 12/15  train_loss=0.28421  test_loss=0.37161  test_cos=0.6284  lr=1.00e-03
02:06:37 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 13/15  train_loss=0.28423  test_loss=0.36926  test_cos=0.6307  lr=1.00e-03
02:06:43 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 14/15  train_loss=0.28426  test_loss=0.36703  test_cos=0.6330  lr=1.00e-03
02:06:49 [INFO] [fastembed-bge-small_to_pplx-embed-1][linear] 15/15  train_loss=0.28428  test_loss=0.36493  test_cos=0.6351  lr=1.00e-03
02:06:54 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 01/15  train_loss=0.32635  test_loss=0.44505  test_cos=0.5550  lr=1.00e-03
02:07:00 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 02/15  train_loss=0.29545  test_loss=0.40950  test_cos=0.5905  lr=1.00e-03
02:07:06 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 03/15  train_loss=0.29369  test_loss=0.39612  test_cos=0.6039  lr=1.00e-03
02:07:11 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 04/15  train_loss=0.29330  test_loss=0.38777  test_cos=0.6122  lr=1.00e-03
02:07:17 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 05/15  train_loss=0.29310  test_loss=0.38224  test_cos=0.6178  lr=1.00e-03
02:07:23 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 06/15  train_loss=0.29295  test_loss=0.37822  test_cos=0.6218  lr=1.00e-03
02:07:28 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 07/15  train_loss=0.29277  test_loss=0.37504  test_cos=0.6250  lr=1.00e-03
02:07:34 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 08/15  train_loss=0.29256  test_loss=0.37240  test_cos=0.6276  lr=1.00e-03
02:07:40 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 09/15  train_loss=0.29231  test_loss=0.37009  test_cos=0.6299  lr=1.00e-03
02:07:45 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 10/15  train_loss=0.29204  test_loss=0.36794  test_cos=0.6321  lr=1.00e-03
02:07:51 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 11/15  train_loss=0.29174  test_loss=0.36587  test_cos=0.6341  lr=1.00e-03
02:07:57 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 12/15  train_loss=0.29143  test_loss=0.36386  test_cos=0.6361  lr=1.00e-03
02:08:02 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 13/15  train_loss=0.29111  test_loss=0.36189  test_cos=0.6381  lr=1.00e-03
02:08:08 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 14/15  train_loss=0.29078  test_loss=0.35995  test_cos=0.6400  lr=1.00e-03
02:08:14 [INFO] [fastembed-bge-small_to_pplx-embed-1][deep] 15/15  train_loss=0.29044  test_loss=0.35802  test_cos=0.6420  lr=1.00e-03
02:08:14 [INFO] [fastembed-bge-small_to_pplx-embed-1] winner=deep best_epoch=15 best_test_cos=0.6420 saved → fastembed-bge-small_to_pplx-embed-1.pt  (173.7s)
02:08:14 [INFO]
─── [49/49] fastembed-bge-small → nemotron-1b-free ───
02:08:14 [INFO] [fastembed-bge-small_to_nemotron-1b-free] 384d → 2048d
02:08:24 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 01/15  train_loss=0.37175  test_loss=0.51815  test_cos=0.4819  lr=1.00e-03
02:08:35 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 02/15  train_loss=0.35466  test_loss=0.50236  test_cos=0.4976  lr=1.00e-03
02:08:45 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 03/15  train_loss=0.35379  test_loss=0.49432  test_cos=0.5057  lr=1.00e-03
02:08:55 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 04/15  train_loss=0.35351  test_loss=0.48825  test_cos=0.5118  lr=1.00e-03
02:09:05 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 05/15  train_loss=0.35338  test_loss=0.48302  test_cos=0.5170  lr=1.00e-03
02:09:15 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 06/15  train_loss=0.35331  test_loss=0.47830  test_cos=0.5217  lr=1.00e-03
02:09:26 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 07/15  train_loss=0.35326  test_loss=0.47395  test_cos=0.5261  lr=1.00e-03
02:09:36 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 08/15  train_loss=0.35323  test_loss=0.46991  test_cos=0.5301  lr=1.00e-03
02:09:46 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 09/15  train_loss=0.35321  test_loss=0.46615  test_cos=0.5338  lr=1.00e-03
02:09:56 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 10/15  train_loss=0.35320  test_loss=0.46264  test_cos=0.5374  lr=1.00e-03
02:10:07 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 11/15  train_loss=0.35320  test_loss=0.45935  test_cos=0.5407  lr=1.00e-03
02:10:17 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 12/15  train_loss=0.35319  test_loss=0.45626  test_cos=0.5437  lr=1.00e-03
02:10:27 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 13/15  train_loss=0.35319  test_loss=0.45336  test_cos=0.5466  lr=1.00e-03
02:10:37 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 14/15  train_loss=0.35319  test_loss=0.45063  test_cos=0.5494  lr=1.00e-03
02:10:47 [INFO] [fastembed-bge-small_to_nemotron-1b-free][linear] 15/15  train_loss=0.35319  test_loss=0.44805  test_cos=0.5519  lr=1.00e-03
02:10:56 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 01/15  train_loss=0.40598  test_loss=0.49619  test_cos=0.5038  lr=1.00e-03
02:11:05 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 02/15  train_loss=0.36977  test_loss=0.47148  test_cos=0.5285  lr=1.00e-03
02:11:15 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 03/15  train_loss=0.36755  test_loss=0.46537  test_cos=0.5346  lr=1.00e-03
02:11:24 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 04/15  train_loss=0.36719  test_loss=0.46484  test_cos=0.5352  lr=1.00e-03
02:11:33 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 05/15  train_loss=0.36696  test_loss=0.46285  test_cos=0.5372  lr=1.00e-03
02:11:42 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 06/15  train_loss=0.36683  test_loss=0.46032  test_cos=0.5397  lr=1.00e-03
02:11:51 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 07/15  train_loss=0.36672  test_loss=0.45847  test_cos=0.5415  lr=1.00e-03
02:12:00 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 08/15  train_loss=0.36663  test_loss=0.45712  test_cos=0.5429  lr=1.00e-03
02:12:09 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 09/15  train_loss=0.36654  test_loss=0.45591  test_cos=0.5441  lr=1.00e-03
02:12:18 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 10/15  train_loss=0.36645  test_loss=0.45469  test_cos=0.5453  lr=1.00e-03
02:12:27 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 11/15  train_loss=0.36635  test_loss=0.45338  test_cos=0.5466  lr=1.00e-03
02:12:37 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 12/15  train_loss=0.36624  test_loss=0.45194  test_cos=0.5481  lr=1.00e-03
02:12:46 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 13/15  train_loss=0.36612  test_loss=0.45040  test_cos=0.5496  lr=1.00e-03
02:12:55 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 14/15  train_loss=0.36599  test_loss=0.44876  test_cos=0.5512  lr=1.00e-03
02:13:04 [INFO] [fastembed-bge-small_to_nemotron-1b-free][deep] 15/15  train_loss=0.36585  test_loss=0.44706  test_cos=0.5529  lr=1.00e-03
02:13:04 [INFO] [fastembed-bge-small_to_nemotron-1b-free] winner=deep best_epoch=15 best_test_cos=0.5529 saved → fastembed-bge-small_to_nemotron-1b-free.pt  (290.2s)
02:13:04 [INFO]
All done in 388.0 min
Models   → /Users/gigadelux/Documents/PROJECTS/queryn/queryn/Adapters/models/v1/
Report   → /Users/gigadelux/Documents/PROJECTS/queryn/queryn/Adapters/reports/v1/training_report.json
