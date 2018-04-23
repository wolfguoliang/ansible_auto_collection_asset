#创建资产存储的表
CREATE TABLE `ansible_host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `manufacturer` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `os` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `cpu_model` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `cpu_count` varchar(10) COLLATE utf8_bin DEFAULT NULL,
  `cpu_core` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `memory_totally` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `swap_totally` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `disk` varchar(200) COLLATE utf8_bin DEFAULT NULL,
  `ip` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `mac_address` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `sn` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
