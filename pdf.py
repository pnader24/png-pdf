from PIL import Image
import os

def convert_png_to_pdf():
    try:
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 构建输入和输出文件的完整路径
        input_path = os.path.join(current_dir, 'sd.png')
        output_path = os.path.join(current_dir, 'sd.pdf')
        
        print(f"正在转换: {input_path}")
        
        # 检查文件是否存在
        if not os.path.exists(input_path):
            print(f"错误: 找不到图片文件。请确保 'sd.png' 位于: {current_dir}")
            return
            
        # 打开PNG图片
        image = Image.open(input_path)
        
        # 如果图片不是RGB模式，转换为RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # 保存为PDF
        image.save(output_path, 'PDF', resolution=100.0)
        print(f"转换成功！PDF已保存到: {output_path}")
        
    except Exception as e:
        print(f"转换过程出错: {str(e)}")

if __name__ == "__main__":
    convert_png_to_pdf()
