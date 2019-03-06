# -*- coding: utf-8 -*-

# C:\Users\Administrator  default windows
#
class ConfigUtil(object):
    def __init__(self, filePath):
        self.filePath = filePath

    def getAllConfig(self):
        data = None
        f = None
        try:
            f = open(self.filePath, mode='rb')
            data = f.read()
        except Exception as ignore:
            pass
        finally:
            if f is not None:
                f.close()
        if data is not None:
            return data.decode(encoding='utf-8')
        return None

    def saveConfig(self, c):
        if isinstance(c, str) is False:
            return
        f = None
        try:
            f = open(self.filePath, mode='wb')
            f.write(c.encode(encoding='utf-8'))
            f.flush()
        except Exception as ignore:
            pass
        finally:
            if f is not None:
                f.close()

