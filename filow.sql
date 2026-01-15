/*
 Navicat Premium Dump SQL

 Source Server         : sqlite
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 13/01/2026 04:19:18
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for _file_organization_old_20260113
-- ----------------------------
DROP TABLE IF EXISTS "_file_organization_old_20260113";
CREATE TABLE "_file_organization_old_20260113" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "extension" TEXT,
  "category" integer,
  "target_folder" TEXT,
  FOREIGN KEY ("category") REFERENCES "category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Records of _file_organization_old_20260113
-- ----------------------------

-- ----------------------------
-- Table structure for actions
-- ----------------------------
DROP TABLE IF EXISTS "actions";
CREATE TABLE "actions" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "filename" TEXT,
  "initial_location" TEXT,
  "last_location" TEXT,
  "time" DATE
);

-- ----------------------------
-- Records of actions
-- ----------------------------

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS "category";
CREATE TABLE "category" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "category_name" TEXT
);

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO "category" VALUES (1, 'Images');
INSERT INTO "category" VALUES (2, 'Document');
INSERT INTO "category" VALUES (3, 'Data');
INSERT INTO "category" VALUES (4, 'Audio');
INSERT INTO "category" VALUES (5, 'Video');
INSERT INTO "category" VALUES (6, 'Archives');
INSERT INTO "category" VALUES (7, 'Code');
INSERT INTO "category" VALUES (8, 'Executables');
INSERT INTO "category" VALUES (9, 'Presentations');

-- ----------------------------
-- Table structure for file_organization
-- ----------------------------
DROP TABLE IF EXISTS "file_organization";
CREATE TABLE "file_organization" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "extension" TEXT,
  "category" integer,
  "custom_path" TEXT,
  "subfolder" TEXT(1),
  FOREIGN KEY ("category") REFERENCES "category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Records of file_organization
-- ----------------------------
INSERT INTO "file_organization" VALUES (1, '.jpg', 1, 'NULL');
INSERT INTO "file_organization" VALUES (2, '.jpeg', 1, 'NULL');
INSERT INTO "file_organization" VALUES (3, '.png', 1, 'NULL');
INSERT INTO "file_organization" VALUES (4, '.gif', 1, 'NULL');
INSERT INTO "file_organization" VALUES (5, '.svg', 1, 'NULL');
INSERT INTO "file_organization" VALUES (6, '.webp', 1, 'NULL');
INSERT INTO "file_organization" VALUES (7, '.bmp', 1, 'NULL');
INSERT INTO "file_organization" VALUES (8, '.tiff', 1, 'NULL');
INSERT INTO "file_organization" VALUES (9, '.raw', 1, 'NULL');
INSERT INTO "file_organization" VALUES (10, '.pdf', 2, 'NULL');
INSERT INTO "file_organization" VALUES (11, '.docx', 2, 'NULL');
INSERT INTO "file_organization" VALUES (12, '.doc', 2, 'NULL');
INSERT INTO "file_organization" VALUES (13, '.txt', 2, 'NULL');
INSERT INTO "file_organization" VALUES (14, '.rtf', 2, 'NULL');
INSERT INTO "file_organization" VALUES (15, '.odt', 2, 'NULL');
INSERT INTO "file_organization" VALUES (16, '.pages', 2, 'NULL');
INSERT INTO "file_organization" VALUES (17, '.xlsx', 3, 'NULL');
INSERT INTO "file_organization" VALUES (18, '.xls', 3, 'NULL');
INSERT INTO "file_organization" VALUES (19, '.csv', 3, 'NULL');
INSERT INTO "file_organization" VALUES (20, '.json', 3, 'NULL');
INSERT INTO "file_organization" VALUES (21, '.xml', 3, 'NULL');
INSERT INTO "file_organization" VALUES (22, '.sql', 3, 'NULL');
INSERT INTO "file_organization" VALUES (23, '.mp3', 4, 'NULL');
INSERT INTO "file_organization" VALUES (24, '.wav', 4, 'NULL');
INSERT INTO "file_organization" VALUES (25, '.flac', 4, 'NULL');
INSERT INTO "file_organization" VALUES (26, '.aac', 4, 'NULL');
INSERT INTO "file_organization" VALUES (27, '.ogg', 4, 'NULL');
INSERT INTO "file_organization" VALUES (28, '.wma', 4, 'NULL');
INSERT INTO "file_organization" VALUES (29, '.mp4', 5, 'NULL');
INSERT INTO "file_organization" VALUES (30, '.mkv', 5, 'NULL');
INSERT INTO "file_organization" VALUES (31, '.avi', 5, 'NULL');
INSERT INTO "file_organization" VALUES (32, '.mov', 5, 'NULL');
INSERT INTO "file_organization" VALUES (33, '.wmv', 5, 'NULL');
INSERT INTO "file_organization" VALUES (34, '.flv', 5, 'NULL');
INSERT INTO "file_organization" VALUES (35, '.webm', 5, 'NULL');
INSERT INTO "file_organization" VALUES (36, 'zip', 6, 'NULL');
INSERT INTO "file_organization" VALUES (37, '.rar', 6, 'NULL');
INSERT INTO "file_organization" VALUES (38, '.7z', 6, 'NULL');
INSERT INTO "file_organization" VALUES (39, '.tar', 6, 'NULL');
INSERT INTO "file_organization" VALUES (40, '.gz', 6, 'NULL');
INSERT INTO "file_organization" VALUES (41, '.py', 7, 'NULL');
INSERT INTO "file_organization" VALUES (42, '.js', 7, 'NULL');
INSERT INTO "file_organization" VALUES (43, '.html', 7, 'NULL');
INSERT INTO "file_organization" VALUES (44, '.css', 7, 'NULL');
INSERT INTO "file_organization" VALUES (45, '.cpp', 7, 'NULL');
INSERT INTO "file_organization" VALUES (46, '.java', 7, 'NULL');
INSERT INTO "file_organization" VALUES (47, '.php', 7, 'NULL');
INSERT INTO "file_organization" VALUES (48, '.sh', 7, 'NULL');
INSERT INTO "file_organization" VALUES (49, '.rs', 7, 'NULL');
INSERT INTO "file_organization" VALUES (50, '.exe', 8, 'NULL');
INSERT INTO "file_organization" VALUES (51, '.msi', 8, 'NULL');
INSERT INTO "file_organization" VALUES (52, '.dmg', 8, 'NULL');
INSERT INTO "file_organization" VALUES (53, '.app', 8, 'NULL');
INSERT INTO "file_organization" VALUES (54, '.deb', 8, 'NULL');
INSERT INTO "file_organization" VALUES (55, '.sh', 8, 'NULL');
INSERT INTO "file_organization" VALUES (56, '.AppImage', 8, 'NULL');
INSERT INTO "file_organization" VALUES (57, '.pptx', 9, 'NULL');
INSERT INTO "file_organization" VALUES (58, '.ppt', 9, 'NULL');
INSERT INTO "file_organization" VALUES (59, '.key', 9, 'NULL');

ALTER TABLE "file_organization" 
ADD COLUMN "subfolder" TEXT(1) DEFAULT '0';