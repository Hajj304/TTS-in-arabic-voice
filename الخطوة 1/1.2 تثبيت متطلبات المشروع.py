# بعض المشاريع تحتوي على ملف requirements.txt
!pip install -r requirements.txt
# error
# إزالة النسخ الحالية
!pip uninstall -y torch torchvision torchaudio

# تثبيت إصدارات متوافقة (CUDA 11.8)
!pip install torch==2.1.0+cu118 torchvision==0.16.0+cu118 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118

