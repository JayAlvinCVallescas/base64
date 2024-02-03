import argparse
import sys
import base64

def encodeBase64(inputString):      
    inputBytes = inputString.encode("ascii")
    base64Bytes = base64.b64encode(inputBytes)
    return base64Bytes.decode("ascii")

def decodeBase64(inputString):
    try:
        base64Bytes = base64.b64decode(inputString)
        decodedString = base64Bytes.decode("ascii")
        return decodedString
    except Exception as e:
        return f"Error decoding: {e}"
    
def main():
    parser = argparse.ArgumentParser(
        description="A Python program that lets you encode and decode base64 text.\n"
                    "Example usage:\n\n"
                    "Encoding:\n"
                    "    python b64.py -e hello\n"
                    "    Result: aGVsbG8=\n\n"
                    "Decoding:\n"
                    "    python b64.py -d aGVsbG8=\n"
                    "    Result: hello",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-e", "--encode", help="Encode base64", metavar="String_Of_Characters")
    parser.add_argument("-d", "--decode", help="Decode base64", metavar="BASE64_STRING")
    args = parser.parse_args()
    
    if args.decode:
        result = decodeBase64(args.decode)
        print(result)
    elif args.encode:
        result = encodeBase64(args.encode)
        print(result)

if __name__ == "__main__":
    main()