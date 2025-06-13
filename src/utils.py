# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/13 10:32
# @File     :utils.py
# @Software :PyCharm
# 工具配置日志模块等
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

from repo_cli.utils.detect import file_handler


def setup_logger(name, log_level=logging.INFO, max_bytes=10 * 1024 * 1024, backup_count = 5):
    """
    配置日志模块（日志轮转，动态日志级别）
    :param name: Logger名称，通常用模块名
    :param log_level: 日志级别，默认INFO
    :param max_bytes: 单个日志文件最大大小，默认10MB
    :param backup_count: 保留备份日志文件数量，默认5个
    :return: 配置好的Logger对象
    """
    # 创建logs目录（如果不存在）
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 日志文件名（按时间命名）
    log_file = f"logs/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    # 日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 文件处理器
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 创建Logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == '__main__':
    # 测试日志轮转功能
    logger = setup_logger("test_logger",log_level=logging.DEBUG)
    for i in range(10000):
        logger.debug(f"Debug message {i}")
        logger.info(f"info message {i}")
        logger.warning(f"Waring message {i}")
        logger.error(f"Error message {i}")
