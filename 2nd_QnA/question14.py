import win32com.client

outlook = win32com.client.Dispatch('Outlook.Application')
namespace = outlook.GetNamespace('MAPI')
inbox_folder = namespace.Folders.Item('ackrite03@naver.com')
