CREATE TABLE products
(
    id          VARCHAR(32) PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    description TEXT,
    price       FLOAT        NOT NULL,
    image_url   TEXT,
    is_active   BOOLEAN   DEFAULT TRUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('43e575329f9811f0ba75acde48001122',
        'Bộ máy tính PC Gaming Core I7 Ram 16Gb, Card GT 730 Chơi Game Liên Minh, Fifa, Đột Kích, Au..', 2850000,
        'images/vn-11134207-7ras8-mdgf7q6f7kj06b_tn.webp', '', TRUE, '2025-10-02 14:01:17.144246',
        '2025-10-02 14:01:17.437903');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4412e15c9f9811f0ba75acde48001122',
        'Bộ máy tính PC GAMING i7 + Ram 16gb + SSD 500gb + CARD RỜI 6G chơi mượt GTA5, PUBG PC..- BH 6 tháng 1 ĐỔI 1',
        5150000, 'images/vn-11134207-7ras8-mdgfu1vl3bxr3d_tn.webp', '', TRUE, '2025-10-02 14:01:17.441911',
        '2025-10-02 14:01:17.486240');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4419fb869f9811f0ba75acde48001122',
        'Bộ máy tính PC Gaming i5 13400f / 12400F + RTX 5060 Ti ram 16GB chiến mọi game, đồ họa - BH 36 Tháng',
        13226000, 'images/vn-11134207-7ras8-mct0ky8aztlo5d_tn.webp', '', TRUE, '2025-10-02 14:01:17.488456',
        '2025-10-02 14:01:17.537204');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4421bb789f9811f0ba75acde48001122',
        'Bộ Máy Tính Gaming  Full Trắng  Core i7 Ram 16Gb Card GTX 750 Chơi Mượt Game LOL, PUBG, FIFA CF AUDITION...',
        3900000, 'images/vn-11134207-7ras8-m1srrfc7ldub74_tn.webp', '', TRUE, '2025-10-02 14:01:17.539242',
        '2025-10-02 14:01:17.582656');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4428a7d09f9811f0ba75acde48001122',
        'Nguyên Bộ Máy Tính Chơi Game Core i7 – Văn Phòng – Đồ Họa Nhẹ – Học Tập Online – Màn LED Đẹp', 2300025,
        'images/vn-11134207-7ras8-mddmuqvb1jn1d4_tn.webp', '', TRUE, '2025-10-02 14:01:17.584616',
        '2025-10-02 14:01:17.659196');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44344e5a9f9811f0ba75acde48001122',
        'Bộ máy tính PC I5 Ram 8gb Full Trắng Làm Việc Đồ Họa, Học Tập, Chơi Game Liên Minh, Fifa,Đột Kích...', 2079000,
        'images/vn-11134207-7ras8-mcmc8nd6iwtpea_tn.webp', '', TRUE, '2025-10-02 14:01:17.660966',
        '2025-10-02 14:01:17.709134');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('443bf3b29f9811f0ba75acde48001122',
        'PC Econo 01 | I5 13400F, 16GB DDR5, 1TB SSD, Wifi + Bluetooth (Mới, BH 36T)', 20100000,
        'images/vn-11134207-820l4-mf7sfizrf3t5df_tn.webp', '', TRUE, '2025-10-02 14:01:17.711075',
        '2025-10-02 14:01:17.759248');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44439cd49f9811f0ba75acde48001122',
        'Máy Tính Bộ DELL Optilex 3050 SFF Core i7 i5 i3 , Ram 8G, SSD 256G ( Bảo hành 1 năm)', 2600000,
        'images/vn-11134207-7ras8-m43uyv4ldrw01f_tn.webp', '', TRUE, '2025-10-02 14:01:17.761279',
        '2025-10-02 14:01:17.791607');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('444885fa9f9811f0ba75acde48001122',
        'Bộ Máy Tính Văn Phòng PC i3,i5,i7 ram 8G 16G SSD 256G Dùng Mượt Mọi Tác Vụ Cơ Bản Có Cài Sẵn Win Và Office - BH 3 năm',
        2590000, 'images/vn-11134207-7ras8-m2vtxia5o168d4_tn.webp', '', TRUE, '2025-10-02 14:01:17.793462',
        '2025-10-02 14:01:17.831796');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('444ebcea9f9811f0ba75acde48001122',
        'PC Gaming FPS 01 | Ryzen 7 5700X, 16GB Ram, VGA RTX 3060 / 5060 / 5060 Ti 16GB Mới BH 36T', 18300000,
        'images/vn-11134207-820l4-me8188wyc5c490_tn.webp', '', TRUE, '2025-10-02 14:01:17.834196',
        '2025-10-02 14:01:17.886698');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44570e049f9811f0ba75acde48001122', 'Thùng PC Gaming Làm Việc WK-10 I5 6500 | VGA GTX 750Ti /RX 550 /RX 580',
        6300000, 'images/vn-11134207-7ras8-m1z14514ona63c_tn.webp', '', TRUE, '2025-10-02 14:01:17.888696',
        '2025-10-02 14:01:17.958942');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44620d229f9811f0ba75acde48001122',
        'Bộ máy tính PC GAMING Đen i7 | Ram 16gb | SSD 500gb | Card 1060 3G chơi mượt GTA5, PUBG PC..', 5300000,
        'images/vn-11134207-820l4-mf234yk85nuw01_tn.webp', '', TRUE, '2025-10-02 14:01:17.960763',
        '2025-10-02 14:01:18.009153');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4469c5da9f9811f0ba75acde48001122',
        'Bộ PC Gaming cân mọi loại game i5 14400f| Main B760m| ram 16G| NVME và256GB', 9200000,
        'images/vn-11134207-820l4-meecq0exm7eoea_tn.webp', '', TRUE, '2025-10-02 14:01:18.011370',
        '2025-10-02 14:01:18.040991');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('446e9d8a9f9811f0ba75acde48001122',
        '[Tặng màn hình FHD 100Hz & Bộ chuột phím Logitech] PC/ Máy tính văn phòng Phong Vũ - Bảo hành 36 tháng',
        7350000, 'images/vn-11134207-7ras8-mdn2ub2et4mp83_tn.webp', '', TRUE, '2025-10-02 14:01:18.043104',
        '2025-10-02 14:01:18.087670');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4475b96c9f9811f0ba75acde48001122',
        'PC Phong Vũ Gaming Cupid M014 (Intel Core i5-12400F/ RTX 3060 / 1 x 16GB/ 512GB SSD/ Free DOS)', 20990000,
        'images/vn-11134207-820l4-mdy9in6jva4h30_tn.webp', '', TRUE, '2025-10-02 14:01:18.089696',
        '2025-10-02 14:01:18.134726');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('447cf65a9f9811f0ba75acde48001122',
        'Combo Đen Cá Tính - Pc bộ Dell Optiplex 3020 SFF & LCD Dell E2216HV - Mạnh mẽ & sang trọng', 3850000,
        'images/sg-11134201-22110-vx2309e9mzjvfe_tn.webp', '', TRUE, '2025-10-02 14:01:18.137129',
        '2025-10-02 14:01:18.185088');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44849b589f9811f0ba75acde48001122', 'Thùng PC Giả Lập Game / MMO NODE 01 | Dual CPU, 64GB Ram (BH 12T)',
        9450000, 'images/vn-11134207-7ra0g-m7jbije3dat8aa_tn.webp', '', TRUE, '2025-10-02 14:01:18.187228',
        '2025-10-02 14:01:18.259118');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('448fe1849f9811f0ba75acde48001122',
        'Bộ PC Máy Tính Robot Gaming Anphat24h i5/i7, Ram 8/16Gb, SSD 256Gb, Card rời 1050Ti/GT730 All Game', 3800000,
        'images/vn-11134207-7ras8-m48n8ht1c9on59_tn.webp', '', TRUE, '2025-10-02 14:01:18.261113',
        '2025-10-02 14:01:18.291160');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('4494c8c09f9811f0ba75acde48001122',
        'Bộ Máy Tính PC  Robot Led i5 i7 ram 8 VGA 1050 chiến game online Fifa, liên minh, gta, aoe đột kích valorant -BH 2 năm',
        4999200, 'images/vn-11134207-7ra0g-ma2tebey23wk7b_tn.webp', '', TRUE, '2025-10-02 14:01:18.293251',
        '2025-10-02 14:01:18.336875');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('449be5569f9811f0ba75acde48001122',
        'Mini PC chạy cpu Intel N100 thế hệ thứ 12 cực mạnh siêu tiết kiệm điện, làm việc văn phòng word excel photoshop',
        3190000, 'images/vn-11134207-7r98o-lkysc9npuvvh57_tn.webp', '', TRUE, '2025-10-02 14:01:18.339869',
        '2025-10-02 14:01:18.390213');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44a417ee9f9811f0ba75acde48001122', 'Thanh lý 15 bộ Pc làm văn phòng HP 800 G3 i5 /8G/SSD 256G Lcd 20icnh',
        4235000, 'images/vn-11134207-7r98o-m08ay5jl2k5rcf_tn.webp', '', TRUE, '2025-10-02 14:01:18.393625',
        '2025-10-02 14:01:18.441236');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44abf4c89f9811f0ba75acde48001122',
        'thùng máy vi tính Dell 390dt chip cpu core i7 2600 ram 8g ssd 120g kết nối vga-hdmi giá chỉ 1750k', 1750000,
        'images/vn-11134207-7ra0g-m7ghjswrwcn00b_tn.webp', '', TRUE, '2025-10-02 14:01:18.445122',
        '2025-10-02 14:01:18.489819');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44b363709f9811f0ba75acde48001122',
        'Thùng PC AURA 02 | Ryzen 7 5700x3D, 16GB Ram | VGA RTX 3050/ RTX 3060/ RTX 4060 Mới BH 36T', 11700000,
        'images/vn-11134207-7ra0g-m7oohex4ikli01_tn.webp', '', TRUE, '2025-10-02 14:01:18.493828',
        '2025-10-02 14:01:18.541736');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44bb162e9f9811f0ba75acde48001122',
        'PC Đồng Bộ Mini Lenovo - Core i3/i5/i7 thế hệ 6+7 - Ram 8GB - SSD 256GB (Tặng Phím+Chuột+USB WIFI)', 2750000,
        'images/vn-11134207-7ras8-m3rbpnjdqoqd1b_tn.webp', '', TRUE, '2025-10-02 14:01:18.544275',
        '2025-10-02 14:01:18.588855');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44c26dd49f9811f0ba75acde48001122', 'Bộ Máy Tính Bàn-PC Intel I3-12100 / B760 / OnBoard Graphic', 5110000,
        'images/vn-11134207-7ra0g-macxtuwtfngsd5_tn.webp', '', TRUE, '2025-10-02 14:01:18.592410',
        '2025-10-02 14:01:18.636676');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44c9ae8c9f9811f0ba75acde48001122',
        'Bộ Máy Tính Văn Phòng PC i3,i5,i7 Ram 8G,16G SSD 128G Dùng Mượt Mọi Tác Vụ Cơ Bản-Mới 100% BH 2 Năm', 2800000,
        'images/vn-11134207-7ras8-m2kw1pjebjcq52_tn.webp', '', TRUE, '2025-10-02 14:01:18.639929',
        '2025-10-02 14:01:18.683343');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44d0a4629f9811f0ba75acde48001122',
        '[HCM] PC Máy Tính Để Bàn Cũ Gía Rẻ Main ASUS P8H61-MX Core I5-3330/ Ram 4GB/ HDD 500GB/ VGA Intel HD Graphics.',
        2090000, 'images/vn-11134211-7ras8-makzvk0xlgwn41_tn.webp', '', TRUE, '2025-10-02 14:01:18.685536',
        '2025-10-02 14:01:18.739850');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44d94c8e9f9811f0ba75acde48001122',
        'Full Bộ PC Gaming Màn hình 180hz Main Asus B760 / i5 12400f / GTX 1660s/ti 6G / Ram 16Gb / SSD 512Gb',
        15518000, 'images/vn-11134207-820l4-mdxgp6zykidj49_tn.webp', '', TRUE, '2025-10-02 14:01:18.742272',
        '2025-10-02 14:01:18.787475');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44e0a42a9f9811f0ba75acde48001122',
        'Bộ PC VSP Gaming Robot Chơi Game Siêu Nhanh Chiến Mọi Game Online Liên Minh fifa valonrant Csgo Đột Kích - BH 2 Năm',
        4999200, 'images/vn-11134207-7ras8-m422u8e9vfxs3b_tn.webp', '', TRUE, '2025-10-02 14:01:18.790393',
        '2025-10-02 14:01:18.848982');
INSERT INTO products (id, name, price, image_url, description, is_active, created_at, updated_at)
VALUES ('44ea31b69f9811f0ba75acde48001122',
        'Thùng PC AURA 01 | Ryzen 5 5600, 16GB Ram | VGA RX 580/ RTX 3050/ RTX 3060 Mới BH 36T', 11100000,
        'images/vn-11134207-7ras8-m2dhkgyxu5kke9_tn.webp', '', TRUE, '2025-10-02 14:01:18.853000',
        '2025-10-02 14:01:18.914890');