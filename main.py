import logging
import sys
import uvicorn

sys.path.insert(0,'./sample_stuff')

def main():
    logging.basicConfig()
    uvicorn.run(
        "sample_stuff.app:app",
        host='0.0.0.0',
        reload=True
    )
    print('goodbye')


if __name__ == '__main__':
    main()
