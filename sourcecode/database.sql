USE [master]
GO
/****** Object:  Database [MMT]    Script Date: 7/21/2022 10:07:33 PM ******/
CREATE DATABASE [MMT]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'MMT', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.VOTHIEN\MSSQL\DATA\MMT.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'MMT_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.VOTHIEN\MSSQL\DATA\MMT_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [MMT] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [MMT].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [MMT] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [MMT] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [MMT] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [MMT] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [MMT] SET ARITHABORT OFF 
GO
ALTER DATABASE [MMT] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [MMT] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [MMT] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [MMT] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [MMT] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [MMT] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [MMT] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [MMT] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [MMT] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [MMT] SET  DISABLE_BROKER 
GO
ALTER DATABASE [MMT] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [MMT] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [MMT] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [MMT] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [MMT] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [MMT] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [MMT] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [MMT] SET RECOVERY FULL 
GO
ALTER DATABASE [MMT] SET  MULTI_USER 
GO
ALTER DATABASE [MMT] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [MMT] SET DB_CHAINING OFF 
GO
ALTER DATABASE [MMT] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [MMT] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [MMT] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [MMT] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'MMT', N'ON'
GO
ALTER DATABASE [MMT] SET QUERY_STORE = OFF
GO
USE [MMT]
GO
/****** Object:  Table [dbo].[DonHang]    Script Date: 7/21/2022 10:07:33 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DonHang](
	[ID] [char](3) NULL,
	[TenKhachHang] [nvarchar](50) NULL,
	[TenKhachSan] [nvarchar](50) NULL,
	[SoLuong] [int] NULL,
	[NgayDen] [datetime] NULL,
	[NgayDi] [datetime] NULL,
	[Tong] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Phong]    Script Date: 7/21/2022 10:07:33 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Phong](
	[ID] [char](3) NULL,
	[LoaiPhong] [nvarchar](50) NULL,
	[TenKhachSan] [nvarchar](50) NULL,
	[Mota] [nvarchar](250) NULL,
	[GiaPhong] [int] NULL,
	[NgayDen] [datetime] NULL,
	[NgayDi] [datetime] NULL,
	[TinhTrang] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TaiKhoan]    Script Date: 7/21/2022 10:07:33 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TaiKhoan](
	[TenDangNhap] [nvarchar](50) NOT NULL,
	[MatKhau] [nvarchar](50) NOT NULL,
	[STK] [char](10) NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'001', N'Thien', N'3/2', 1, CAST(N'2002-01-01T00:00:00.000' AS DateTime), CAST(N'2002-01-02T00:00:00.000' AS DateTime), NULL)
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'001', N'thien', N'3/2', 2, CAST(N'2003-01-01T00:00:00.000' AS DateTime), CAST(N'2004-01-01T00:00:00.000' AS DateTime), NULL)
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'001', N'ThienVo', N'3/2', 2, CAST(N'2002-01-02T00:00:00.000' AS DateTime), CAST(N'2003-01-02T00:00:00.000' AS DateTime), NULL)
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'001', N'Thien', N'3/2', 2, CAST(N'2002-03-02T00:00:00.000' AS DateTime), CAST(N'2004-03-03T00:00:00.000' AS DateTime), NULL)
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'002', N'Thien', N'Ha long', 2, CAST(N'2002-01-01T00:00:00.000' AS DateTime), CAST(N'2003-01-02T00:00:00.000' AS DateTime), NULL)
INSERT [dbo].[DonHang] ([ID], [TenKhachHang], [TenKhachSan], [SoLuong], [NgayDen], [NgayDi], [Tong]) VALUES (N'001', N'thien', N'3/2', 1, CAST(N'2002-01-01T00:00:00.000' AS DateTime), CAST(N'2003-01-02T00:00:00.000' AS DateTime), NULL)
GO
INSERT [dbo].[Phong] ([ID], [LoaiPhong], [TenKhachSan], [Mota], [GiaPhong], [NgayDen], [NgayDi], [TinhTrang]) VALUES (N'001', N'Vip', N'3/2', N'Sang, sạch, đẹp', 2000, CAST(N'2002-01-01T00:00:00.000' AS DateTime), CAST(N'2003-01-02T00:00:00.000' AS DateTime), 1)
INSERT [dbo].[Phong] ([ID], [LoaiPhong], [TenKhachSan], [Mota], [GiaPhong], [NgayDen], [NgayDi], [TinhTrang]) VALUES (N'002', N'Thuong', N'Ha Long', N'2 giường ngủ', 4000, CAST(N'2002-01-01T00:00:00.000' AS DateTime), CAST(N'2003-01-02T00:00:00.000' AS DateTime), 1)
GO
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [STK]) VALUES (N'a', N'1', N'12345     ')
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [STK]) VALUES (N'b', N'2', N'34        ')
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [STK]) VALUES (N'abc', N'123', N'1234567891')
GO
USE [master]
GO
ALTER DATABASE [MMT] SET  READ_WRITE 
GO
