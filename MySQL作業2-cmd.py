import pymysql
import prettytable
import os

table = prettytable.PrettyTable(["Memberserial","Name","Birthday","Address"], encodong = "utf8")

def ShowMemberList():
	#每次執行此函式都先清除table
	table.clear_rows()
	cursor.execute("SELECT * FROM `member`")
	data = cursor.fetchall()
	# print(data)
	for show in data:
		table.add_row([show[0],show[1],show[2],show[3]])
	print(table)

def AddNewMember(Name, Birthday, Address):
	addmemberlist = [Name, Birthday, Address]
	sql = "INSERT INTO `member`(`name`,`birthday`,`address`) Values(%s,%s,%s)"
	cursor.execute(sql, addmemberlist)
	# 有改變動作完要加的(新增/刪除/更改值)
	database.commit()
	os.system("cls")
	print("新增完成！！\n")
	return "新增完成！！"

def RenewMember(ID, Name, Birthday, Address):
	ReMemberlist = [Name, Birthday, Address, ID]
	sql = "UPDATE `member` SET `name`= %s,`birthday`= %s,`address`= %s WHERE `id`= %s"
	cursor.execute(sql, ReMemberlist)
	database.commit()
	os.system("cls")
	print("更新完成！！\n")
	return "更新完成！！"

def DeleteMember(ID):
	DeleteList = [ID]
	sql = "DELETE FROM `member` WHERE `id`= %s"
	cursor.execute(sql, DeleteList)
	database.commit()
	os.system("cls")
	print("刪除完成！！\n")
	return "刪除完成！！"

def CommendSelect(num_str, ID = None, Name = None, Birthday = None, Address = None):
	command = {"0":os.system, "1":ShowMemberList, "2":AddNewMember, "3":RenewMember, "4":DeleteMember}
	function = command.get(num_str)
	if function:
		if num_str == "0":
			function("exit")
		elif num_str == "1":
			function()
		elif num_str == "2":
			function(Name, Birthday, Address)
		elif num_str == "3":
			function(ID, Name, Birthday, Address)
		elif num_str == "4":
			function(ID)

# 開啟資料庫連線
database = pymysql.connect(
	host = "localhost",
	user = "root",
	password = "",
	db = "python_ai",
	charset = "utf8"
)
# 使用 cursor() 方法建立一個遊標物件 cursor
cursor = database.cursor()

# #創建新Table
# cursor.execute("CREATE TABLE MemberSystem(Name char(50), Birthday date, Age int,Address text")

commandmsg = "(0)離開程式\n(1)顯示會員列表\n(2)新增會員資料\n(3)更新會員資料\n(4)刪除會員資料\n請輸入指令："
connect = False

while True:
	#確認是否有連線到資料庫
	cursor.execute("SELECT VERSION()")
	# 使用 fetchone() 獲取單條資料
	data = cursor.fetchone()
	# print("Database version :", data[0])
	if data != []:
		connect = True
		inputcommand = input(commandmsg)
		try:
			int(inputcommand)
			if 0 <= int(inputcommand) <= 4:
				if inputcommand == "0":
					os.system("cls")
					# 關閉資料庫連線
					database.close()
					CommendSelect(inputcommand)
					break
				elif inputcommand == "1":
					os.system("cls")
					CommendSelect(inputcommand)
				elif inputcommand == "2":
					os.system("cls")
					n_name = input("請輸入新進會員名字：")
					n_birthday = input("請輸入新進會員生日：")
					n_address = input("請輸入新進會員地址：")
					CommendSelect(inputcommand, Name = n_name, Birthday = n_birthday, Address = n_address)
				elif inputcommand == "3":
					os.system("cls")
					print(table)
					re_id = input("請輸入欲修改的會員編號：")
					re_name = input("請輸入欲修改的會員名字：")
					re_birthday = input("請輸入欲修改的會員生日：")
					re_address = input("請輸入欲修改的會員地址：")
					CommendSelect(inputcommand, ID = re_id, Name = re_name, Birthday = re_birthday, Address = re_address)
				elif inputcommand == "4":
					os.system("cls")
					print(table)
					del_id = input("請輸入欲刪除的會員編號：")
					CommendSelect(inputcommand, ID = del_id)
			else:
				os.system("cls")
				print("沒有這個指令！！\n")
		except:
			os.system("cls")
			print("請輸入正確指令！！\n")

	else:
		connect = False
		database = pymysql.connect(
			host = "localhost",
			user = "root",
			password = "",
			db = "python_ai",
			charset = "utf8"
		)
		cursor = database.cursor()
