from setuptools import setup, find_packages

setup(
    name='qaznlp',
    version='4.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'transformers>=4.37.2',
        'torch>=1.13.1',
        'flask>=2.1.0',
        'flasgger>=0.9.5',
        'tokenizers>=0.13.3',
        'sentencepiece>=0.1.99',
        'tqdm>=4.64.1',
        'scikit-learn>=1.1.2',
        'numpy>=1.23.5',
        'pandas>=1.4.4',
        'onnx>=1.12.0',
        'onnxruntime>=1.14.1'
    ],
    author='Aigerim',
    description='QazNLP: Full-featured NLP suite for Kazakh language',
    license='MIT',
    python_requires='>=3.8',
)