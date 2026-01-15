const { Client } = require('discord.js-selfbot-v13');
const client = new Client({ checkUpdate: false });

const TOKEN = "MTM5OTcyMTAyNTU1Nzc2MjE3MA.GRDL-w.NpVpKeMowaqi9MSlT2Y1VF3v6onVLXsobbr1Ek";
const PREFIX = "!";

// --- KHO NGÔN SIÊU CẤP ---
const KHO_NGON = [
    "# S AY", "# SUA E", "# LE E", "# MANH MA", "# PHE AK", "# TK GA", "# S VAY", "# SUA CAI",
    "# LE MA", "# O KIA", "# TK NGU", "# MANH K", "# SLOW AK", "# SPEED DEI", "# PHE V",
    "# OC C", "# CN DI", "# TAT AK", "# CLM", "# PHE VAT", "# SUA MAU", "# EM RAI",
    "# MANH CAI", "# LE CAI", "# S DO", "# MANH DI", "# YEU V", "# RUN AK", "# KENG NGAY",
    "# KENG MA", "# SUA K", "# SUA AK", "# SUA DE", "# MANH CHU", "# MANH NUA", "# S KIA",
    "# SON MAU", "# LE MAU", "# HANG CAI", "# SON K", "# SON AK", "# MANH AK", "# DUOI AK",
    "# CCHO", "# CO TI", "# LE TI", "# CHAT MAU", "# KENG K", "# KENG AK", "# LE NUA",
    "# SUA NUA", "# SON CAI", "# TK DU", "# DU AK", "# LO LO", "# ON K", "# K AK", "# O O",
    "# CHAM V", "# LAG AK", "# NGU V", "# KAKA", "# R X", "# WIN AK", "# VTR AK", "# NOTI AK",
    "# EZ V", "# EI EI", "# CHAT K", "# CHAT AK", "# HANG DEI", "# BAI AK", "# EI KU",
    "# DIT MM", "# SO AK", "# RUM AK", "# LE K", "# KEM V", "# MAU NAO", "# SON LE",
    "# HANG DE", "# MANH DE", "# CAY AK", "# NGU CAY", "# MET AK", "# KMM", "# SUA LEN",
    "# SON LEN", "# NGU AK", "# LE EI", "# LE NAO", "# SUA CHU", "# TK OC", "# CHAT MAU",
    "# GA CON", "# TUOI GI", "# CON GA", "# KHOC DI", "# DUNG SUA", "# CAM MOM"
];

client.on('ready', () => {
    console.log("================================");
    console.log(`✅ KHANG GOD NGON ONLINE: ${client.user.tag}`);
    console.log("👉 Gõ !khang @tên để xả ngôn");
    console.log("================================");
});

client.on('messageCreate', async (message) => {
    if (message.author.id !== client.user.id) return;
    if (!message.content.startsWith(PREFIX)) return;

    const args = message.content.slice(PREFIX.length).trim().split(/ +/);
    const command = args.shift().toLowerCase();

    if (command === 'khang') {
        const user = message.mentions.users.first();
        if (!user) return message.reply("Tag thằng cần dập vào anh ơi!");

        await message.delete().catch(() => {});
        console.log(`🔥 ĐANG DẬP: ${user.username}`);

        // Vòng lặp xả ngôn vô hạn
        while (true) {
            // Bốc 3 câu ngẫu nhiên ghép lại
            const n1 = KHO_NGON[Math.floor(Math.random() * KHO_NGON.length)];
            const n2 = KHO_NGON[Math.floor(Math.random() * KHO_NGON.length)];
            const n3 = KHO_NGON[Math.floor(Math.random() * KHO_NGON.length)];

            const content = `**${n1}** | **${n2}** | **${n3}** <@${user.id}>`;

            try {
                await message.channel.send(content);
                // Tốc độ 0.7 giây (chỉnh thấp hơn nếu muốn nhanh hơn)
                await new Promise(r => setTimeout(r, 000));
            } catch (e) {
                console.log("Bị chậm lại chút...");
                await new Promise(r => setTimeout(r, 2000));
            }
        }
    }
});

client.login(TOKEN);
