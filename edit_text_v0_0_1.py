import sys
import math
import struct
import random
import zlib
import urllib.parse

if sys.version_info.major<3 or (sys.version_info.minor<=5 and sys.version_info.major==3):
    print('本程序使用格式化字符串(f""),Python3.5及以下不支持此特性,如果出现了这个提示,请尝试更新你的Python版本!')
    exit()
class UnknownArgs(Exception):
    """自定义异常：未知的命令行参数。"""
    pass

class Text():
    """文本替换工具类。

    提供字符和字符串级别的查找替换功能。
    """
    class MyTools:
        @staticmethod
        def Right_To_Left(text)->str:
            """将字符串从右到左反转
            Args:
                text (str):  输入字符串
            Returns:
                str:  反转后的字符串
            Examples:
                >>> Classic_Tools.Text.Right_To_Left("123456")
                '654321'
            """
            text = str(text)
            return text[::-1]

        @staticmethod
        def Right_To_Left_Old(text)->str:
            """将字符串从右到左反转
            Args:
                text (str):  输入字符串
            Returns:
                str:  反转后的字符串
            Examples:
                >>> Classic_Tools.Text.Right_To_Left_Old("123456")
                '654321'
            """
            text = str(text)
            a=""
            for i in range(len(text)):
                a+=text[len(text)-(i+1)]
            return a

        @staticmethod
        def Base10(Hex:str,Base:int):
            """
            将特定进制数字转为base10
            Args:
                Base (int):  进制
                Hex (str):  Base进制的数字
            Returns:
                由Base进制的数字转为base10的数字
            Examples:
                >>> Classic_Tools.Text.Base10("1A",16)
                26
                >>> Classic_Tools.Text.Base10("1010",2)
                10
            """
            try:
                return int(str(Hex),int(Base))
            except Exception as e:
                print(e)

        @staticmethod
        def Random_16Hex(num:int,Not_Zero=True):
            """
            生成随机16进制数字
            Args:
                num (int):  随机数字长度
                Not_Zero (bool):  是否包含0
            Returns:
                str:  随机16进制数字
            Examples:
                >>> Classic_Tools.Text.Random_16Hex(4)
                '1A3B'
                >>> Classic_Tools.Text.Random_16Hex(4,False)
                '01A3B'
            """
            HexNum=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
            if not Not_Zero:
                HexNum.insert(0,"0")
            try:
                a=''
                num=int(num)
                for i in range(num):
                    if i == 1 and Not_Zero:
                        HexNum.insert(0,"0")
                    a+=random.choice(HexNum)
                return a
            except Exception as e:
                print("错误",e)

        @staticmethod
        def random_password()->str:
            """
            生成随机密码
            Args:
                None
            Returns:
                str:  随机密码
            Examples:
                >>> Classic_Tools.Text.random_password()
                'DGs8ads$!=pNm3Q'
            """
            pwd_text=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
 , "!", "_","$","&","+","=","-"]
            text=""
            for i in range(random.randint(12,20)):
                text+=random.choice(pwd_text)
            return text
        
    class Replace():
        """替换操作集合。"""

        class string():
            """字符串替换操作。"""

            @staticmethod
            def All_string(text, string, string2):
                """将文本中所有匹配的子串替换为指定字符串。

                Args:
                    text (str): 原始文本。
                    string (str): 要查找的子串。
                    string2 (str): 替换成的字符串。

                Returns:
                    str: 替换后的文本。无匹配时原样返回。出错时返回空字符串。

                Example:
                    >>> Text.Replace.string.All_string('hello world', 'world', 'Python')
                    'hello Python'
                """
                try:
                    text = str(text)
                    string = str(string)
                    string2 = str(string2)
                except TypeError:
                    print("请输入文本😡")
                    return ''
                return text.replace(string, string2)

            @staticmethod
            def place_string(text, string, string2, place):
                """在文本的指定位置替换子串。

                从指定索引开始，将匹配的旧子串替换为新字符串。
                如果该位置的内容与旧子串不匹配，则返回原文本。

                Args:
                    text (str): 原始文本。
                    string (str): 要替换的旧子串。
                    string2 (str): 替换成的新字符串。
                    place (int): 起始替换位置（索引）。

                Returns:
                    str: 替换后的文本。若该位置内容不匹配则返回原文本。
                    出错时返回空字符串。

                Example:
                    >>> Text.Replace.string.place_string('hello world', 'world', 'Python', 6)
                    'hello Python'
                    >>> Text.Replace.string.place_string('hello world', 'world', 'Python', 0)
                    'hello world'
                """
                try:
                    text = str(text)
                    string = str(string)
                    string2 = str(string2)
                    place = int(place)
                except (TypeError, ValueError):
                    print("请输入文本/数字😡")
                    return ''
                end = place + len(string)
                if place < 0 or end > len(text) or text[place:end] != string:
                    return text
                return text[:place] + string2 + text[end:]

            @staticmethod
            def precise_place_string(text, string, string2, place):
                """将文本中第 N 次出现的子串替换为指定字符串。

                基于出现次数查找替换，而非字符索引位置。
                如果第 N 次出现不存在，则返回原文本。

                Args:
                    text (str): 原始文本。
                    string (str): 要查找的旧子串。
                    string2 (str): 替换成的新字符串。
                    place (int): 第几次出现（从 0 开始计数）。

                Returns:
                    str: 替换后的文本。若不存在第 N 次则返回原文本。
                    出错时返回空字符串。

                Example:
                    >>> Text.Replace.string.precise_place_string('aa_aa_aa', 'aa', 'x', 0)
                    'x_aa_aa'
                    >>> Text.Replace.string.precise_place_string('aa_aa_aa', 'aa', 'x', 1)
                    'aa_x_aa'
                    >>> Text.Replace.string.precise_place_string('aa_aa_aa', 'aa', 'x', 5)
                    'aa_aa_aa'
                """
                try:
                    text = str(text)
                    string = str(string)
                    string2 = str(string2)
                    place = int(place)
                except (TypeError, ValueError):
                    print("请输入文本/数字😡")
                    return ''
                count = 0
                i = 0
                while i <= len(text):
                    if text[i:i + len(string)] == string:
                        if count == place:
                            return text[:i] + string2 + text[i + len(string):]
                        count += 1
                        i += len(string)
                    else:
                        i += 1
                return text


    class Case():
        """大小写转换。

        提供字符串的全大写、全小写和标题格式转换。
        """
        @staticmethod
        def upper(text):
            """将文本转换为全大写。

            Args:
                text (str): 输入文本。

            Returns:
                str: 全大写后的文本。

            Example:
                >>> Text.Case.upper('hello')
                'HELLO'
            """
            return str(text).upper()
        @staticmethod
        def lower(text):
            """将文本转换为全小写。

            Args:
                text (str): 输入文本。

            Returns:
                str: 全小写后的文本。

            Example:
                >>> Text.Case.lower('HELLO')
                'hello'
            """
            return str(text).lower()
        @staticmethod
        def title(text):
            """将文本转换为标题格式（每个单词首字母大写）。

            Args:
                text (str): 输入文本。

            Returns:
                str: 标题格式后的文本。

            Example:
                >>> Text.Case.title('hello world')
                'Hello World'
            """
            return str(text).title()

    class Count():
        """文本统计工具。

        统计文本的字符数、单词数和行数。
        """
        @staticmethod
        def count(text):
            """统计文本的字符数、单词数和行数。

            Args:
                text (str): 输入文本。

            Returns:
                str: 包含字符数、单词数和行数的格式化结果。

            Example:
                >>> Text.Count.count('hello\nworld')
                '字符: 11\n单词: 2\n行数: 2'
            """
            text = str(text)
            chars = len(text)
            words = len(text.split())
            lines = text.count('\n') + 1
            return f"字符: {chars}\n单词: {words}\n行数: {lines}"

    class Sort():
        """文本行排序工具。

        支持普通排序和排序后去重。
        """
        @staticmethod
        def sort(text, uniq=False):
            """对文本行进行排序（可选去重）。

            Args:
                text (str): 输入文本，按换行符分隔。
                uniq (bool): 是否去重，默认为 False。

            Returns:
                str: 排序后的文本。

            Example:
                >>> Text.Sort.sort('b\na\nc\na')
                'a\nb\nc\na'
                >>> Text.Sort.sort('b\na\nc\na', True)
                'a\nb\nc'
            """
            lines = str(text).split('\n')
            lines.sort()
            if uniq:
                result = []
                seen = set()
                for line in lines:
                    if line not in seen:
                        result.append(line)
                        seen.add(line)
                return '\n'.join(result)
            return '\n'.join(lines)

    class Split():
        """文本分隔工具。

        将文本按指定分隔符拆分并截取指定段。
        """
        @staticmethod
        def split(text, delimiter, index):
            """将文本按分隔符拆分后截取指定段。

            Args:
                text (str): 输入文本。
                delimiter (str): 分隔符。
                index (int): 要截取的段索引（从 0 开始）。

            Returns:
                str: 指定段的文本。索引越界时返回原文本。

            Example:
                >>> Text.Split.split('a,b,c', ',', 1)
                'b'
            """
            parts = str(text).split(str(delimiter))
            try:
                return parts[int(index)]
            except IndexError:
                return text

class ROT():
    """ROT 旋转加密工具类。

    提供 ASCII 凯撒密码和 Unicode 码点偏移两种旋转加密方式。
    """

    @staticmethod
    def Ascii(code, text):
        """将文本中的 ASCII 字母按指定偏移量循环移位（凯撒密码）。

        保留大小写，非字母字符原样输出。只支持 ASCII 字母（A-Z, a-z）。
        可用于简单的文本加密/解密。

        Args:
            code (int | str): 偏移量。若传入字符串会自动转为整数。
            text (str): 要处理的文本。

        Returns:
            str: 移位后的文本。出错时返回空字符串。

        Example:
            >>> ROT.Ascii(13, 'Hello, World!')
            'Uryyb, Jbeyq!'
        """
        try:
            code = int(code)
        except (TypeError, ValueError):
            print("码数请输入数字!")
            return ''
        text = str(text)
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i + c)] = chr((i + code) % 26 + c)
        return "".join([d.get(c, c) for c in text])

    @staticmethod
    def Unicode(code, text):
        """将文本中每个字符的 Unicode 码点偏移指定值。

        与 :meth:`ROT` 不同，此方法操作原始 Unicode 码点，因此会影响所有字符
        （字母、标点、emoji 等），不限于 ASCII 字母。可用于简单的文本混淆。

        Args:
            code (int | str): 码点偏移量。若传入字符串会自动转为整数。
            text (str): 要处理的文本。

        Returns:
            str: 偏移后的文本。出错时返回空字符串。

        Example:
            >>> ROT.Unicode(1, 'ABC')
            'BCD'
            >>> ROT.Unicode(127894, '🐕')
            '🐣'
        """
        try:
            code = int(code)
        except (TypeError, ValueError):
            print("码数请输入数字!")
            return ''
        text = str(text)
        result = []
        for _ in range(len(text)):
            result.append(chr(ord(text[_]) + code))
        return ''.join(result)


class Base64():
    """Base64 编解码工具类。

    提供标准的 Base64 编码和解码功能（使用 A-Z, a-z, 0-9, +, / 字符集）。
    解码时自动处理填充符 ``=``。
    """

    @staticmethod
    def decode(text):
        """将 Base64 编码的字符串解码为原始文本。

        Args:
            text (str): Base64 编码字符串（可含 ``=`` 填充）。

        Returns:
            str | bytes: 解码结果。若能以 UTF-8 解码则返回字符串，
            否则返回原始字节序列。

        Example:
            >>> Base64.decode('SGVsbG8sIFdvcmxkIQ==')
            'Hello, World!'
        """
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        char_to_index = {}
        for i, char in enumerate(base64_chars):
            char_to_index[char] = i

        text = text.strip()

        padding = 0
        if text.endswith('=='):
            padding = 2
            text = text[:-2]
        elif text.endswith('='):
            padding = 1
            text = text[:-1]

        result_bytes = []
        i = 0
        n = len(text)

        while i < n:
            chunk = text[i:i+4]
            chunk_len = len(chunk)

            values = [0, 0, 0, 0]
            for j in range(chunk_len):
                values[j] = char_to_index.get(chunk[j], 0)

            byte1 = (values[0] << 2) | (values[1] >> 4)
            result_bytes.append(byte1)

            if chunk_len > 2:
                byte2 = ((values[1] & 0xF) << 4) | (values[2] >> 2)
                result_bytes.append(byte2)

            if chunk_len > 3:
                byte3 = ((values[2] & 0x3) << 6) | values[3]
                result_bytes.append(byte3)

            i += 4

        if padding > 0:
            result_bytes = result_bytes[:-padding]

        try:
            return bytes(result_bytes).decode('utf-8')
        except:
            return bytes(result_bytes)

    @staticmethod
    def encode(text):
        """将文本编码为 Base64 字符串。

        Args:
            text (str): 要编码的文本（自动以 UTF-8 编码）。

        Returns:
            str: Base64 编码后的字符串（含 ``=`` 填充）。

        Example:
            >>> Base64.base64_encode('Hello, World!')
            'SGVsbG8sIFdvcmxkIQ=='
        """
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        bytes_data = text.encode('utf-8')

        binary_str = ""
        for byte in bytes_data:
            for j in range(7, -1, -1):
                if byte & (1 << j):
                    binary_str += "1"
                else:
                    binary_str += "0"

        while len(binary_str) % 6 != 0:
            binary_str += "0"

        result = ""
        for i in range(0, len(binary_str), 6):
            chunk = binary_str[i:i+6]
            value = 0
            for j in range(6):
                if chunk[j] == '1':
                    value += 1 << (5 - j)
            result += base64_chars[value]

        while len(result) % 4 != 0:
            result += "="

        return result


class Hash():
    """哈希算法工具类。

    提供 MD5 等哈希函数的实现。
    """

    @staticmethod
    def MD5(message, warning=True):
        """计算指定消息的 MD5 哈希值（仅供实验参考）。

        实现了标准的 MD5 哈希算法，输出 32 位十六进制字符串。
        首次调用时会打印 MD5 已被攻破的安全警告（可关闭）。

        Warning:
            MD5 早在 2004 年已被攻破，可人为制造碰撞漏洞。
            完全不适合任何安全相关用途，仅供实验参考！

        Args:
            message (str): 要计算哈希的消息。
            warning (bool): 是否显示安全警告，默认为 True。

        Returns:
            str: 32 位小写十六进制 MD5 哈希值。

        Example:
            >>> Hash.MD5('Hello, World!')
            '65a8e27d8879283831b664bd8b7f0ad4'
        """
        message = str(message)
        if warning:
            print('\033[91m')
            print(r"""
 __          __              _
 \ \        / /             (_)
  \ \  /\  / /_ _ _ __ _ __  _ _ __   __ _
   \ \/  \/ / _` | '__| '_ \| | '_ \ / _` |
    \  /\  / (_| | |  | | | | | | | | (_| |
     \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                      __/ |
                                     |___/ """)
            print("警告!MD5在很早之前就被攻破,可随意制造碰撞漏洞,完全不适合任何安全相关用途,仅供于实验参考!!!\033[0m")
        A = 0x67452301
        B = 0xEFCDAB89
        C = 0x98BADCFE
        D = 0x10325476
        s = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]
        K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

        def F(x, y, z):
            return (x & y) | (~x & z)

        def G(x, y, z):
            return (x & z) | (y & ~z)

        def H(x, y, z):
            return x ^ y ^ z

        def I(x, y, z):
            return y ^ (x | ~z)

        def left_rotate(x, n):
            return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 512 != 448:
            msg += b'\x00'
        msg += struct.pack('<Q', orig_len)

        for chunk_start in range(0, len(msg), 64):
            chunk = msg[chunk_start:chunk_start + 64]
            M = struct.unpack('<16I', chunk)
            a, b, c, d = A, B, C, D

            for i in range(64):
                if i < 16:
                    f = F(b, c, d)
                    g = i
                elif i < 32:
                    f = G(b, c, d)
                    g = (5 * i + 1) % 16
                elif i < 48:
                    f = H(b, c, d)
                    g = (3 * i + 5) % 16
                else:
                    f = I(b, c, d)
                    g = (7 * i) % 16

                f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
                a = d
                d = c
                c = b
                b = (b + left_rotate(f, s[i])) & 0xFFFFFFFF

            A = (A + a) & 0xFFFFFFFF
            B = (B + b) & 0xFFFFFFFF
            C = (C + c) & 0xFFFFFFFF
            D = (D + d) & 0xFFFFFFFF

        result = struct.pack('<4I', A, B, C, D)
        return result.hex()

    @staticmethod
    def RIPEMD160(message, warning=True):
        """计算指定消息的 RIPEMD-160 哈希值（仅供实验参考）。

        实现了标准的 RIPEMD-160 哈希算法，输出 40 位十六进制字符串。

        Warning:
            RIPEMD-160 安全余量已被严重削弱，安全性不如 SHA1。
            完全不适合任何安全相关用途，仅供实验参考！

        Args:
            message (str): 要计算哈希的消息。
            warning (bool): 是否显示安全警告，默认为 True。

        Returns:
            str: 40 位小写十六进制 RIPEMD-160 哈希值。
        """
        message = str(message)
        if warning:
            print('\033[91m')
            print(r"""
 __          __              _
 \ \        / /             (_)
  \ \  /\  / /_ _ _ __ _ __  _ _ __   __ _
   \ \/  \/ / _` | '__| '_ \| | '_ \ / _` |
    \  /\  / (_| | |  | | | | | | | | (_| |
     \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                      __/ |
                                     |___/ """)
            print("警告!RIPEMD160在2026年安全余量已被严重削弱,且被认为安全性不如SHA1,完全不适合任何安全相关用途,仅供于实验参考!!!\033[0m")
        def left_rotate(x, n):
            return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

        def f1(x, y, z):
            return x ^ y ^ z

        def f2(x, y, z):
            return (x & y) | (~x & z)

        def f3(x, y, z):
            return (x | ~y) ^ z

        def f4(x, y, z):
            return (x & z) | (y & ~z)

        def f5(x, y, z):
            return x ^ (y | ~z)

        K1 = 0x00000000
        K2 = 0x5A827999
        K3 = 0x6ED9EBA1
        K4 = 0x8F1BBCDC
        K5 = 0xA953FD4E

        K1P = 0x50A28BE6
        K2P = 0x5C4DD124
        K3P = 0x6D703EF3
        K4P = 0x7A6D76E9
        K5P = 0x00000000

        ML = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8,
            3, 10, 14, 4, 9, 15, 8, 1, 2, 7, 0, 6, 13, 11, 5, 12,
            1, 9, 11, 10, 0, 8, 12, 4, 13, 3, 7, 15, 14, 5, 6, 2,
            4, 0, 5, 9, 7, 12, 2, 10, 14, 1, 3, 8, 11, 6, 15, 13
        ]

        MR = [
            5, 14, 7, 0, 9, 2, 11, 4, 13, 6, 15, 8, 1, 10, 3, 12,
            6, 11, 3, 7, 0, 13, 5, 10, 14, 15, 8, 12, 4, 9, 1, 2,
            15, 5, 1, 3, 7, 14, 6, 9, 11, 8, 12, 2, 10, 0, 4, 13,
            8, 6, 4, 1, 3, 11, 15, 0, 5, 12, 2, 13, 9, 7, 10, 14,
            12, 15, 10, 4, 1, 5, 8, 7, 6, 2, 13, 14, 0, 3, 9, 11
        ]

        SL = [
            11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8,
            7, 6, 8, 13, 11, 9, 7, 15, 7, 12, 15, 9, 11, 7, 13, 12,
            11, 13, 6, 7, 14, 9, 13, 15, 14, 8, 13, 6, 5, 12, 7, 5,
            11, 12, 14, 15, 14, 15, 9, 8, 9, 14, 5, 6, 8, 6, 5, 12,
            9, 15, 5, 11, 6, 8, 13, 12, 5, 12, 13, 14, 11, 8, 5, 6
        ]

        SR = [
            8, 9, 9, 11, 13, 15, 15, 5, 7, 7, 8, 11, 14, 14, 12, 6,
            9, 13, 15, 7, 12, 8, 9, 11, 7, 7, 12, 7, 6, 15, 13, 11,
            9, 7, 15, 11, 8, 6, 6, 14, 12, 13, 5, 14, 13, 13, 7, 5,
            15, 5, 8, 11, 14, 14, 6, 14, 6, 9, 12, 9, 12, 5, 15, 8,
            8, 5, 12, 9, 12, 5, 14, 6, 8, 13, 6, 5, 15, 13, 11, 11
        ]

        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 512 != 448:
            msg += b'\x00'
        msg += struct.pack('<Q', orig_len)

        for chunk_start in range(0, len(msg), 64):
            chunk = msg[chunk_start:chunk_start + 64]
            X = struct.unpack('<16I', chunk)

            al, bl, cl, dl, el = h0, h1, h2, h3, h4
            ar, br, cr, dr, er = h0, h1, h2, h3, h4

            for j in range(80):
                rnd = j >> 4

                if rnd == 0:
                    fl = f1(bl, cl, dl)
                    fr = f5(br, cr, dr)
                    kl = K1
                    kr = K1P
                elif rnd == 1:
                    fl = f2(bl, cl, dl)
                    fr = f4(br, cr, dr)
                    kl = K2
                    kr = K2P
                elif rnd == 2:
                    fl = f3(bl, cl, dl)
                    fr = f3(br, cr, dr)
                    kl = K3
                    kr = K3P
                elif rnd == 3:
                    fl = f4(bl, cl, dl)
                    fr = f2(br, cr, dr)
                    kl = K4
                    kr = K4P
                elif rnd == 4:
                    fl = f5(bl, cl, dl)
                    fr = f1(br, cr, dr)
                    kl = K5
                    kr = K5P

                T = (al + fl + X[ML[j]] + kl) & 0xFFFFFFFF
                al = (left_rotate(T, SL[j]) + el) & 0xFFFFFFFF
                al, bl, cl, dl, el = el, al, bl, left_rotate(cl, 10), dl

                T = (ar + fr + X[MR[j]] + kr) & 0xFFFFFFFF
                ar = (left_rotate(T, SR[j]) + er) & 0xFFFFFFFF
                ar, br, cr, dr, er = er, ar, br, left_rotate(cr, 10), dr

            T = (h1 + cl + dr) & 0xFFFFFFFF
            h1 = (h2 + dl + er) & 0xFFFFFFFF
            h2 = (h3 + el + ar) & 0xFFFFFFFF
            h3 = (h4 + al + br) & 0xFFFFFFFF
            h4 = (h0 + bl + cr) & 0xFFFFFFFF
            h0 = T

        result = struct.pack('<5I', h0, h1, h2, h3, h4)
        return result.hex()

    @staticmethod
    def sha1(message, warning=True):
        """计算指定消息的 SHA-1 哈希值（仅供实验参考）。

        实现了标准的 SHA-1 哈希算法，输出 40 位十六进制字符串。

        Warning:
            SHA-1 自 2017 年已被实际碰撞攻击攻破（SHAttered），
            不断有新的 CVE 漏洞被发现。不适合任何安全相关用途！

        Args:
            message (str): 要计算哈希的消息。
            warning (bool): 是否显示安全警告，默认为 True。

        Returns:
            str: 40 位小写十六进制 SHA-1 哈希值。
        """
        message = str(message)
        if warning:
            print('\033[91m')
            print(r"""
 __          __              _
 \ \        / /             (_)
  \ \  /\  / /_ _ _ __ _ __  _ _ __   __ _
   \ \/  \/ / _` | '__| '_ \| | '_ \ / _` |
    \  /\  / (_| | |  | | | | | | | | (_| |
     \/  \/ \__,_|_|  |_| |_|_|_| |_|\__, |
                                      __/ |
                                     |___/ """)
            print("""警告!SHA1早在2017年,由Google和CWI Amsterdam联合发起的 “SHAttered” 攻击,就首次实现了对完整SHA-1算法的实际碰撞攻击
不应再用于任何安全相关的场景，
即便到了2026年，仍不断有新的CVE漏洞
仅供于实验参考!!!
\033[0m""")
        def left_rotate(x, n):
            return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 512 != 448:
            msg += b'\x00'
        msg += struct.pack('>Q', orig_len)

        for chunk_start in range(0, len(msg), 64):
            chunk = msg[chunk_start:chunk_start + 64]
            W = list(struct.unpack('>16I', chunk)) + [0] * 64

            for i in range(16, 80):
                W[i] = left_rotate(W[i-3] ^ W[i-8] ^ W[i-14] ^ W[i-16], 1)

            a, b, c, d, e = h0, h1, h2, h3, h4

            for i in range(80):
                if i < 20:
                    f = (b & c) | (~b & d)
                    k = 0x5A827999
                elif i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = (left_rotate(a, 5) + f + e + k + W[i]) & 0xFFFFFFFF
                e = d
                d = c
                c = left_rotate(b, 30)
                b = a
                a = temp

            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF

        return struct.pack('>5I', h0, h1, h2, h3, h4).hex()

    @staticmethod
    def sha256(message):#这很安全
        message=str(message)
        def right_rotate(x, n):
            return (x >> n) | ((x << (32 - n)) & 0xFFFFFFFF)

        h0 = 0x6A09E667
        h1 = 0xBB67AE85
        h2 = 0x3C6EF372
        h3 = 0xA54FF53A
        h4 = 0x510E527F
        h5 = 0x9B05688C
        h6 = 0x1F83D9AB
        h7 = 0x5BE0CD19

        K = [
            0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
            0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
            0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
            0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
            0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
            0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
            0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
            0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
            0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
            0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
            0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
            0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
            0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
            0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
            0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
            0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2
        ]

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 512 != 448:
            msg += b'\x00'
        msg += struct.pack('>Q', orig_len)

        for chunk_start in range(0, len(msg), 64):
            chunk = msg[chunk_start:chunk_start + 64]
            W = list(struct.unpack('>16I', chunk)) + [0] * 48

            for i in range(16, 64):
                s0 = right_rotate(W[i-15], 7) ^ right_rotate(W[i-15], 18) ^ (W[i-15] >> 3)
                s1 = right_rotate(W[i-2], 17) ^ right_rotate(W[i-2], 19) ^ (W[i-2] >> 10)
                W[i] = (W[i-16] + s0 + W[i-7] + s1) & 0xFFFFFFFF

            a, b, c, d = h0, h1, h2, h3
            e, f, g, h = h4, h5, h6, h7

            for i in range(64):
                S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
                ch = (e & f) ^ (~e & g)
                temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFF
                S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) & 0xFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFF

            h0 = (h0 + a) & 0xFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFF

        return struct.pack('>8I', h0, h1, h2, h3, h4, h5, h6, h7).hex()

    @staticmethod
    @staticmethod
    def sha512(message):
        """计算指定消息的 SHA-512 哈希值。

        SHA-512 是 SHA-2 家族成员，目前仍被认为是安全的。
        实现了标准算法，输出 128 位十六进制字符串。

        Args:
            message (str): 要计算哈希的消息。

        Returns:
            str: 128 位小写十六进制 SHA-512 哈希值。
        """
        message=str(message)
        def right_rotate(x, n):
            return (x >> n) | ((x << (64 - n)) & 0xFFFFFFFFFFFFFFFF)

        h0 = 0x6A09E667F3BCC908
        h1 = 0xBB67AE8584CAA73B
        h2 = 0x3C6EF372FE94F82B
        h3 = 0xA54FF53A5F1D36F1
        h4 = 0x510E527FADE682D1
        h5 = 0x9B05688C2B3E6C1F
        h6 = 0x1F83D9ABFB41BD6B
        h7 = 0x5BE0CD19137E2179

        K = [
            0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC,
            0x3956C25BF348B538, 0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118,
            0xD807AA98A3030242, 0x12835B0145706FBE, 0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2,
            0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235, 0xC19BF174CF692694,
            0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,
            0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5,
            0x983E5152EE66DFAB, 0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4,
            0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 0x06CA6351E003826F, 0x142929670A0E6E70,
            0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 0x53380D139D95B3DF,
            0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,
            0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30,
            0xD192E819D6EF5218, 0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8,
            0x19A4C116B8D2D0C8, 0x1E376C085141AB53, 0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8,
            0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373, 0x682E6FF3D6B2B8A3,
            0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,
            0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B,
            0xCA273ECEEA26619C, 0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178,
            0x06F067AA72176FBA, 0x0A637DC5A2C898A6, 0x113F9804BEF90DAE, 0x1B710B35131C471B,
            0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC, 0x431D67C49C100D4C,
            0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817
        ]

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 1024 != 896:
            msg += b'\x00'
        msg += struct.pack('>QQ', 0, orig_len)

        for chunk_start in range(0, len(msg), 128):
            chunk = msg[chunk_start:chunk_start + 128]
            W = list(struct.unpack('>16Q', chunk)) + [0] * 64

            for i in range(16, 80):
                s0 = right_rotate(W[i-15], 1) ^ right_rotate(W[i-15], 8) ^ (W[i-15] >> 7)
                s1 = right_rotate(W[i-2], 19) ^ right_rotate(W[i-2], 61) ^ (W[i-2] >> 6)
                W[i] = (W[i-16] + s0 + W[i-7] + s1) & 0xFFFFFFFFFFFFFFFF

            a, b, c, d = h0, h1, h2, h3
            e, f, g, h = h4, h5, h6, h7

            for i in range(80):
                S1 = right_rotate(e, 14) ^ right_rotate(e, 18) ^ right_rotate(e, 41)
                ch = (e & f) ^ (~e & g)
                temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFFFFFFFFFF
                S0 = right_rotate(a, 28) ^ right_rotate(a, 34) ^ right_rotate(a, 39)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

            h0 = (h0 + a) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFFFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFFFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFFFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFFFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFFFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFFFFFFFFFF

        return struct.pack('>8Q', h0, h1, h2, h3, h4, h5, h6, h7).hex()

    @staticmethod
    def sha384(message):
        """计算指定消息的 SHA-384 哈希值。

        SHA-384 是 SHA-2 家族成员（SHA-512 的截断版本），
        目前仍被认为是安全的。输出 96 位十六进制字符串。

        Args:
            message (str): 要计算哈希的消息。

        Returns:
            str: 96 位小写十六进制 SHA-384 哈希值。
        """
        message=str(message)
        def right_rotate(x, n):
            return (x >> n) | ((x << (64 - n)) & 0xFFFFFFFFFFFFFFFF)

        h0 = 0xCBBB9D5DC1059ED8
        h1 = 0x629A292A367CD507
        h2 = 0x9159015A3070DD17
        h3 = 0x152FECD8F70E5939
        h4 = 0x67332667FFC00B31
        h5 = 0x8EB44A8768581511
        h6 = 0xDB0C2E0D64F98FA7
        h7 = 0x47B5481DBEFA4FA4

        K = [
            0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC,
            0x3956C25BF348B538, 0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118,
            0xD807AA98A3030242, 0x12835B0145706FBE, 0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2,
            0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235, 0xC19BF174CF692694,
            0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,
            0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5,
            0x983E5152EE66DFAB, 0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4,
            0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 0x06CA6351E003826F, 0x142929670A0E6E70,
            0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 0x53380D139D95B3DF,
            0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,
            0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30,
            0xD192E819D6EF5218, 0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8,
            0x19A4C116B8D2D0C8, 0x1E376C085141AB53, 0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8,
            0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373, 0x682E6FF3D6B2B8A3,
            0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,
            0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B,
            0xCA273ECEEA26619C, 0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178,
            0x06F067AA72176FBA, 0x0A637DC5A2C898A6, 0x113F9804BEF90DAE, 0x1B710B35131C471B,
            0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC, 0x431D67C49C100D4C,
            0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817
        ]

        msg = message.encode('utf-8')
        orig_len = len(msg) * 8
        msg += b'\x80'
        while (len(msg) * 8) % 1024 != 896:
            msg += b'\x00'
        msg += struct.pack('>QQ', 0, orig_len)

        for chunk_start in range(0, len(msg), 128):
            chunk = msg[chunk_start:chunk_start + 128]
            W = list(struct.unpack('>16Q', chunk)) + [0] * 64

            for i in range(16, 80):
                s0 = right_rotate(W[i-15], 1) ^ right_rotate(W[i-15], 8) ^ (W[i-15] >> 7)
                s1 = right_rotate(W[i-2], 19) ^ right_rotate(W[i-2], 61) ^ (W[i-2] >> 6)
                W[i] = (W[i-16] + s0 + W[i-7] + s1) & 0xFFFFFFFFFFFFFFFF

            a, b, c, d = h0, h1, h2, h3
            e, f, g, h = h4, h5, h6, h7

            for i in range(80):
                S1 = right_rotate(e, 14) ^ right_rotate(e, 18) ^ right_rotate(e, 41)
                ch = (e & f) ^ (~e & g)
                temp1 = (h + S1 + ch + K[i] + W[i]) & 0xFFFFFFFFFFFFFFFF
                S0 = right_rotate(a, 28) ^ right_rotate(a, 34) ^ right_rotate(a, 39)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

            h0 = (h0 + a) & 0xFFFFFFFFFFFFFFFF
            h1 = (h1 + b) & 0xFFFFFFFFFFFFFFFF
            h2 = (h2 + c) & 0xFFFFFFFFFFFFFFFF
            h3 = (h3 + d) & 0xFFFFFFFFFFFFFFFF
            h4 = (h4 + e) & 0xFFFFFFFFFFFFFFFF
            h5 = (h5 + f) & 0xFFFFFFFFFFFFFFFF
            h6 = (h6 + g) & 0xFFFFFFFFFFFFFFFF
            h7 = (h7 + h) & 0xFFFFFFFFFFFFFFFF

        return struct.pack('>8Q', h0, h1, h2, h3, h4, h5, h6, h7).hex()[:96]


class URL():
    """URL 编解码工具类。

    提供标准的 URL 百分号编码（Percent-encoding）和解码功能。
    """
    @staticmethod
    def encode(text):
        """将文本进行 URL 编码。

        Args:
            text (str): 要编码的文本。

        Returns:
            str: URL 编码后的字符串。

        Example:
            >>> URL.encode('你好')
            '%E4%BD%A0%E5%A5%BD'
        """
        return urllib.parse.quote(str(text), safe='')
    @staticmethod
    def decode(text):
        """将 URL 编码的字符串解码为原始文本。

        Args:
            text (str): URL 编码字符串。

        Returns:
            str: 解码后的原始文本。

        Example:
            >>> URL.decode('%E4%BD%A0%E5%A5%BD')
            '你好'
        """
        return urllib.parse.unquote(str(text))

class Hex():
    """十六进制编解码工具类。

    提供 UTF-8 文本与十六进制字符串之间的相互转换。
    """
    @staticmethod
    def encode(text):
        """将文本编码为十六进制字符串。

        Args:
            text (str): 要编码的文本。

        Returns:
            str: 十六进制编码字符串。

        Example:
            >>> Hex.encode('Hello')
            '48656c6c6f'
        """
        return str(text).encode('utf-8').hex()
    @staticmethod
    def decode(text):
        """将十六进制字符串解码为原始文本。

        Args:
            text (str): 十六进制编码字符串。

        Returns:
            str: 解码后的原始文本。

        Example:
            >>> Hex.decode('48656c6c6f')
            'Hello'
        """
        return bytes.fromhex(str(text)).decode('utf-8')

class Bin():
    """二进制编解码工具类。

    提供 UTF-8 文本与二进制字符串（如 ``01001000``）之间的相互转换。
    """
    @staticmethod
    def encode(text):
        """将文本编码为二进制字符串（每字节 8 位，空格分隔）。

        Args:
            text (str): 要编码的文本。

        Returns:
            str: 二进制编码字符串。

        Example:
            >>> Bin.encode('Hi')
            '01001000 01101001'
        """
        return ' '.join(format(b, '08b') for b in str(text).encode('utf-8'))
    @staticmethod
    def decode(text):
        """将二进制字符串解码为原始文本。

        Args:
            text (str): 二进制编码字符串（每字节 8 位，空格分隔）。

        Returns:
            str: 解码后的原始文本。

        Example:
            >>> Bin.decode('01001000 01101001')
            'Hi'
        """
        bins = str(text).split()
        return bytes(int(b, 2) for b in bins).decode('utf-8')

class Morse():
    """摩斯电码编解码。"""
    _MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '@': '.--.-.', ' ': '/'
    }
    _MORSE_REV = {v: k for k, v in _MORSE_CODE.items()}

    @staticmethod
    def encode(text):
        """将文本编码为摩斯电码。

        Args:
            text (str): 要编码的文本（自动转为大写）。

        Returns:
            str: 摩斯电码字符串，各符号间以空格分隔。

        Example:
            >>> Morse.encode('SOS')
            '... --- ...'
        """
        text = str(text).upper()
        result = []
        for char in text:
            if char in Morse._MORSE_CODE:
                result.append(Morse._MORSE_CODE[char])
            else:
                result.append(char)
        return ' '.join(result)

    @staticmethod
    def decode(text):
        """将摩斯电码解码为原始文本。

        Args:
            text (str): 摩斯电码字符串，各符号间以空格分隔。

        Returns:
            str: 解码后的文本。

        Example:
            >>> Morse.decode('... --- ...')
            'SOS'
        """
        result = []
        for code in str(text).split(' '):
            if code in Morse._MORSE_REV:
                result.append(Morse._MORSE_REV[code])
            elif code == '':
                continue
            else:
                result.append(code)
        return ''.join(result)

class Atbash():
    """Atbash 密码 (字母表反转)。"""
    @staticmethod
    def cipher(text):
        """对文本应用 Atbash 密码（字母表反转）。

        大写字母映射到对应的大写反转字母，小写映射到小写反转字母，
        非字母字符保持不变。

        Args:
            text (str): 输入文本。

        Returns:
            str: Atbash 加密/解密后的文本（加解密使用同一函数）。

        Example:
            >>> Atbash.cipher('Hello')
            'Svool'
        """
        result = []
        for char in str(text):
            if 'A' <= char <= 'Z':
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            elif 'a' <= char <= 'z':
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)

class XOR():
    """XOR 加解密工具。

    使用 XOR 算法对文本加解密，输出为十六进制字符串。
    加解密使用同一函数，对密文再次执行 XOR 即可还原。
    """
    @staticmethod
    def cipher(text, key):
        """对文本进行 XOR 加解密。

        Args:
            text (str): 明文或密文（十六进制字符串）。
            key (str): 密钥。

        Returns:
            str: 加密/解密后的十六进制字符串。对结果再次用相同密钥执行会还原。

        Example:
            >>> XOR.cipher('Hello', 'key')
            '230015070a'
            >>> XOR.cipher('230015070a', 'key')  # 注意: 输入为十六进制字符串
        """
        text_bytes = str(text).encode('utf-8')
        key_bytes = str(key).encode('utf-8')
        result = bytes(text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes)))
        return result.hex()

class CRC32():
    """CRC32 校验工具类。

    提供 32 位循环冗余校验值计算。
    """
    @staticmethod
    def crc32(text):
        """计算文本的 CRC32 校验值。

        Args:
            text (str): 输入文本。

        Returns:
            str: 8 位十六进制 CRC32 校验值。

        Example:
            >>> CRC32.crc32('Hello')
            'f7d18982'
        """
        return format(zlib.crc32(str(text).encode('utf-8')) & 0xFFFFFFFF, '08x')

class FileTools():
    """文件操作工具类。

    提供文本文件的读取、写入、哈希计算和编码转换功能。
    """
    @staticmethod
    def read(path):
        """读取文本文件内容。

        Args:
            path (str): 文件路径。

        Returns:
            str: 文件内容（UTF-8 编码）。

        Example:
            >>> FileTools.read('test.txt')
            'Hello World'
        """
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def write(path, content):
        """将内容写入文本文件。

        Args:
            path (str): 文件路径。
            content (str): 要写入的内容。

        Returns:
            str: 写入成功的提示信息。

        Example:
            >>> FileTools.write('test.txt', 'Hello')
            '[OK] 已写入 test.txt'
        """
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"[OK] 已写入 {path}"

    @staticmethod
    def hash(path, algo):
        """计算文本文件的哈希值。

        Args:
            path (str): 文件路径。
            algo (str): 哈希算法 (md5/sha1/sha256/sha384/sha512/ripemd160/crc32)。

        Returns:
            str: 哈希值字符串。不支持算法时返回错误提示。

        Example:
            >>> FileTools.hash('test.txt', 'sha256')
            'e3b0c44298fc1c149afbf4c8996fb924...'
        """
        with open(path, 'rb') as f:
            data = f.read()
        text = data.decode('utf-8')
        algo = algo.lower()
        if algo == 'md5':
            return Hash.MD5(text)
        elif algo == 'sha1':
            return Hash.sha1(text)
        elif algo == 'sha256':
            return Hash.sha256(text)
        elif algo == 'sha384':
            return Hash.sha384(text)
        elif algo == 'sha512':
            return Hash.sha512(text)
        elif algo == 'ripemd160':
            return Hash.RIPEMD160(text)
        elif algo == 'crc32':
            return CRC32.crc32(text)
        else:
            return f"[错误] 不支持哈希算法: {algo}"

    @staticmethod
    def encode(path, enc):
        """将文本文件编码为指定格式。

        Args:
            path (str): 文件路径。
            enc (str): 编码格式 (base64/hex/bin)。

        Returns:
            str: 编码后的字符串。不支持编码时返回错误提示。

        Example:
            >>> FileTools.encode('test.txt', 'base64')
            'SGVsbG8='
        """
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        enc = enc.lower()
        if enc == 'base64':
            return Base64.encode(data)
        elif enc == 'hex':
            return Hex.encode(data)
        elif enc == 'bin':
            return Bin.encode(data)
        else:
            return f"[错误] 不支持编码: {enc}"

class Stats():
    """文本统计 & 阅读时间估算工具类。

    统计文本的字符数、单词数、行数，并根据平均阅读速度（300 词/分钟）
    估算阅读所需时间。
    """
    @staticmethod
    def stats(text):
        """统计文本信息并估算阅读时间。

        Args:
            text (str): 输入文本。

        Returns:
            str: 包含字符数、单词数、行数和预估阅读时间的格式化结果。

        Example:
            >>> Stats.stats('Hello world')
            '字符: 11\n单词: 2\n行数: 1\n预估阅读时间: 1 秒'
        """
        text = str(text)
        chars = len(text)
        words = len(text.split())
        lines = text.count('\n') + 1
        read_time = words / 300
        if read_time < 1:
            read_time_str = f"{read_time * 60:.0f} 秒"
        else:
            read_time_str = f"{read_time:.1f} 分钟"
        return f"字符: {chars}\n单词: {words}\n行数: {lines}\n预估阅读时间: {read_time_str}"

def rainbow():
    """输出 256 色彩虹文字。

    将 "我是劲爆彩虹" 重复至 256 个字符，每个字符以不同 ANSI
    颜色输出，形成彩虹渐变效果。

    Args:
        None

    Returns:
        None: 直接输出到控制台。

    Example:
        >>> rainbow()
        # 在支持 ANSI 颜色的终端中显示彩色文字
    """
    text=list("我是劲爆彩虹"*99)
    for i in range(256):
        print(f"\033[38;5;{i}m {text[i]}",end='')

if __name__ == "__main__":
    try:
        #==帮助==
        if sys.argv[1] == "--help":
            print(r"""
 edit_text Beta — 文本编辑工具

 用法:
     --version                   显示版本号
     --help                      显示此帮助

 加密 / 编码:
     --rot ascii <偏移> <文本>     凯撒密码 (ASCII字母)
     --rot unicode <偏移> <文本>    Unicode码点偏移
     --base64 encode <文本>         Base64编码
     --base64 decode <文本>         Base64解码
     --url encode <文本>            URL编码
     --url decode <文本>            URL解码
     --hex encode <文本>            十六进制编码
     --hex decode <文本>            十六进制解码
     --bin encode <文本>            二进制编码
     --bin decode <文本>            二进制解码
     --morse encode <文本>          摩斯电码编码
     --morse decode <文本>          摩斯电码解码
     --atbash <文本>                Atbash字母反转密码
     --xor <密钥> <文本>            XOR加解密

 哈希:
     --hash md5 <文本> [warning]         MD5
     --hash sha1 <文本> [warning]        SHA-1
     --hash sha256 <文本>                SHA-256
     --hash sha384 <文本>                SHA-384
     --hash sha512 <文本>                SHA-512
     --hash ripemd160 <文本> [warning]   RIPEMD-160
     --hash crc32 <文本>                 CRC32

 文本操作:
     --text replace all <文本> <旧> <新>               全部替换
     --text replace place <文本> <旧> <新> <位置>      指定索引替换
     --text replace precise_place <文本> <旧> <新> <N>  第N次出现替换
     --text case <upper|lower|title> <文本>            大小写转换
     --text count <文本>                               字符/单词/行数统计
     --text sort [uniq] <文本>                         文本行排序
     --text split <分隔符> <N> <文本>                  文本截取指定段

 工具:
     --tools reverse <文本>                    反转字符串
     --tools base10 <数字> <进制>              任意进制转十进制
     --tools randhex <长度> [nozero]           随机十六进制数
     --tools randpwd                           生成随机密码

 文件操作:
     --file read <路径>                   读取文本文件
     --file write <路径> <内容>           写入文本文件
     --file hash <路径> <算法>            计算文件哈希
     --file encode <路径> <编码>          文件编码(base64|hex|bin)

 其他:
     --stats <文本>                        文本统计 & 阅读时间估算
     --rainbow                             彩虹输出 (～￣▽￣)～

 示例:
     edit_text --rot ascii 13 Hello
     edit_text --rot unicode 5 你好
     edit_text --base64 encode 哈基米
     edit_text --url encode 你好
     edit_text --hex encode Hello
     edit_text --bin encode Hello
     edit_text --morse encode SOS
     edit_text --atbash Hello
     edit_text --xor key Hello
     edit_text --hash md5 哈基米
     edit_text --hash sha256 哈基米
     edit_text --hash crc32 哈基米
     edit_text --text count "你好 world"
     edit_text --text sort uniq "b\na\nb"
     edit_text --text split "," 1 "a,b,c"
     edit_text --tools reverse 123456
     edit_text --tools base10 1A 16
     edit_text --tools randhex 8
     edit_text --tools randpwd
     edit_text --file read test.txt
     edit_text --file hash test.txt sha256
     edit_text --stats "你好 world hello"
     edit_text --rainbow
""")

        #==版本==
        elif sys.argv[1] == "--version":
            try:
                with open("version.txt") as f:
                    ver = f.read().strip()
                print(ver)
            except:
                print("edit_text v0.0.1")

        #==ROT旋转加密==
        elif sys.argv[1] == "--rot":
            if sys.argv[2] == "unicode":
                if sys.argv[3] and sys.argv[4]:
                    print(ROT.Unicode(sys.argv[3], sys.argv[4]))
            elif sys.argv[2] == "ascii":
                if sys.argv[3] and sys.argv[4]:
                    print(ROT.Ascii(sys.argv[3], sys.argv[4]))
            else:
                raise UnknownArgs

        #==Base64编解码==
        elif sys.argv[1] == "--base64":
            if sys.argv[2] == "encode":
                if sys.argv[3]:
                    print(Base64.encode(sys.argv[3]))
            elif sys.argv[2] == "decode":
                if sys.argv[3]:
                    print(Base64.decode(sys.argv[3]))
            else:
                raise UnknownArgs

        #==哈希==
        elif sys.argv[1] == "--hash":
            if sys.argv[2] == "md5":
                if sys.argv[3]:
                    try:
                        if str(sys.argv[4]):
                            print(Hash.MD5(sys.argv[3], sys.argv[4]))
                    except IndexError:
                        print(Hash.MD5(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "sha1":
                if sys.argv[3]:
                    try:
                        if str(sys.argv[4]):
                            print(Hash.sha1(sys.argv[3], sys.argv[4]))
                    except IndexError:
                        print(Hash.sha1(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "sha256":
                if sys.argv[3]:
                    print(Hash.sha256(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "sha384":
                if sys.argv[3]:
                    print(Hash.sha384(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "sha512":
                if sys.argv[3]:
                    print(Hash.sha512(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "ripemd160":
                if sys.argv[3]:
                    try:
                        if str(sys.argv[4]):
                            print(Hash.RIPEMD160(sys.argv[3], sys.argv[4]))
                    except IndexError:
                        print(Hash.RIPEMD160(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "crc32":
                if sys.argv[3]:
                    print(CRC32.crc32(sys.argv[3]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==文本操作==
        elif sys.argv[1] == "--text":
            if sys.argv[2] == "replace":
                if sys.argv[3] == "all":
                    if sys.argv[4] and sys.argv[5] and sys.argv[6]:
                        print(Text.Replace.string.All_string(sys.argv[4], sys.argv[5], sys.argv[6]))
                    else:
                        raise UnknownArgs
                elif sys.argv[3] == "place":
                    if sys.argv[4] and sys.argv[5] and sys.argv[6] and sys.argv[7]:
                        print(Text.Replace.string.place_string(sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]))
                    else:
                        raise UnknownArgs
                elif sys.argv[3] == "precise_place":
                    if sys.argv[4] and sys.argv[5] and sys.argv[6] and sys.argv[7]:
                        print(Text.Replace.string.precise_place_string(sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]))
                    else:
                        raise UnknownArgs
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "case":
                if sys.argv[3] and sys.argv[4]:
                    if sys.argv[3] == "upper":
                        print(Text.Case.upper(sys.argv[4]))
                    elif sys.argv[3] == "lower":
                        print(Text.Case.lower(sys.argv[4]))
                    elif sys.argv[3] == "title":
                        print(Text.Case.title(sys.argv[4]))
                    else:
                        raise UnknownArgs
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "count":
                if sys.argv[3]:
                    print(Text.Count.count(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "sort":
                if sys.argv[3]:
                    try:
                        if sys.argv[3] == "uniq":
                            print(Text.Sort.sort(sys.argv[4], True))
                        else:
                            raise UnknownArgs
                    except IndexError:
                        print(Text.Sort.sort(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "split":
                if sys.argv[3] and sys.argv[4] and sys.argv[5]:
                    print(Text.Split.split(sys.argv[5], sys.argv[3], sys.argv[4]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==工具==
        elif sys.argv[1] == "--tools":
            if sys.argv[2] == "reverse":
                if sys.argv[3]:
                    print(Text.MyTools.Right_To_Left(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "base10":
                if sys.argv[3] and sys.argv[4]:
                    print(Text.MyTools.Base10(sys.argv[3], sys.argv[4]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "randhex":
                if sys.argv[3]:
                    try:
                        if sys.argv[4] == "nozero":
                            print(Text.MyTools.Random_16Hex(sys.argv[3], False))
                        else:
                            raise UnknownArgs
                    except IndexError:
                        print(Text.MyTools.Random_16Hex(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "randpwd":
                print(Text.MyTools.random_password())
            else:
                raise UnknownArgs

        #==URL编解码==
        elif sys.argv[1] == "--url":
            if sys.argv[2] == "encode":
                if sys.argv[3]:
                    print(URL.encode(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "decode":
                if sys.argv[3]:
                    print(URL.decode(sys.argv[3]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==Hex编解码==
        elif sys.argv[1] == "--hex":
            if sys.argv[2] == "encode":
                if sys.argv[3]:
                    print(Hex.encode(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "decode":
                if sys.argv[3]:
                    print(Hex.decode(sys.argv[3]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==二进制编解码==
        elif sys.argv[1] == "--bin":
            if sys.argv[2] == "encode":
                if sys.argv[3]:
                    print(Bin.encode(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "decode":
                if sys.argv[3]:
                    print(Bin.decode(sys.argv[3]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==摩斯电码==
        elif sys.argv[1] == "--morse":
            if sys.argv[2] == "encode":
                if sys.argv[3]:
                    print(Morse.encode(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "decode":
                if sys.argv[3]:
                    print(Morse.decode(sys.argv[3]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==Atbash==
        elif sys.argv[1] == "--atbash":
            if sys.argv[2]:
                print(Atbash.cipher(sys.argv[2]))
            else:
                raise UnknownArgs

        #==XOR==
        elif sys.argv[1] == "--xor":
            if sys.argv[2] and sys.argv[3]:
                print(XOR.cipher(sys.argv[3], sys.argv[2]))
            else:
                raise UnknownArgs

        #==文件操作==
        elif sys.argv[1] == "--file":
            if sys.argv[2] == "read":
                if sys.argv[3]:
                    print(FileTools.read(sys.argv[3]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "write":
                if sys.argv[3] and sys.argv[4]:
                    print(FileTools.write(sys.argv[3], sys.argv[4]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "hash":
                if sys.argv[3] and sys.argv[4]:
                    print(FileTools.hash(sys.argv[3], sys.argv[4]))
                else:
                    raise UnknownArgs
            elif sys.argv[2] == "encode":
                if sys.argv[3] and sys.argv[4]:
                    print(FileTools.encode(sys.argv[3], sys.argv[4]))
                else:
                    raise UnknownArgs
            else:
                raise UnknownArgs

        #==Stats==
        elif sys.argv[1] == "--stats":
            if sys.argv[2]:
                print(Stats.stats(sys.argv[2]))
            else:
                raise UnknownArgs

        #==Rainbow==
        elif sys.argv[1] == "--rainbow":
            rainbow()

        else:
            raise UnknownArgs

    except (UnknownArgs, IndexError):
        print('未知参数，输入"--help"获取帮助')
r"""
  _______ _                 _          
 |__   __| |               | |       _ 
    | |  | |__   __ _ _ __ | | _____(_)
    | |  | '_ \ / _` | '_ \| |/ / __|  
    | |  | | | | (_| | | | |   <\__ \_ 
    |_|  |_| |_|\__,_|_| |_|_|\_\___(_)

Zhixie(me)
Deepseek-v4-flash
and You             
"""