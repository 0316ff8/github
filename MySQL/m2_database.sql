create database db01;-- 創建資料庫db01
CREATE SCHEMA `db02` ;-- 創建資料庫db02

use db01;-- 切換資料庫db01
show char set;-- 顯示字元集
show databases;-- 顯示所有資料庫
show collation;-- 顯示所有支援的collation
show collation like '%utf8mb4%';-- 校對名稱為utf8mb4的collation
show collation like '%big5%';-- 校對名稱為big5的collation

alter database db02
character set big5
collate big5_chinese_ci;-- 修改資料庫db02,字元集為big5,替換為big5_chinese_ci

select @@character_set_database,@@collation_database;-- 查詢目前資料庫字元集
drop database db02;-- 刪除資料庫db02