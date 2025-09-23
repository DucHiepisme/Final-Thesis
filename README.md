# Football Foul Detection System - Final Thesis

## 🎯 Project Overview

This project implements an automated system for detecting fouls in football (soccer) videos using computer vision and machine learning techniques. The system analyzes video footage to identify potential foul incidents, making it valuable for sports analysis, referee assistance, and match review processes.

## 🏗️ System Architecture

The project consists of several key components:

- **Frame Extraction**: Extracting frames from video footage at specified intervals
- **Preprocessing**: Data preparation and augmentation for model training
- **Feature Extraction**: Using Vision Transformer (ViT) for visual feature extraction
- **Classification**: Binary classification to detect foul vs non-foul incidents
- **Workflow Management**: Orchestrating the entire pipeline from video input to foul detection

## 📁 Project Structure

```
Final Thesis/
├── Code/
│   ├── main.py                 # Main entry point
│   ├── config/
│   │   └── prompt.yml          # Configuration settings
│   ├── src/
│   │   ├── constants.py        # Project constants
│   │   ├── preprocess/         # Data preprocessing modules
│   │   │   └── frame_collector.py  # Frame extraction utilities
│   │   ├── utils/              # Utility functions
│   │   │   └── subvideo.py     # Video processing utilities
│   │   └── workflow/           # Main workflow orchestration
│   ├── cache/                  # Cached data and models
│   │   ├── moments/            # Extracted moment data
│   │   ├── subs/               # Subtitle data
│   │   ├── val/                # Validation data
│   │   │   ├── foul/           # Foul examples
│   │   │   └── no_foul/        # Non-foul examples
│   │   └── vit_custom_augmented_focuscam/  # Trained model
│   ├── result/                 # Output results
│   │   ├── frame/              # Extracted frames
│   │   ├── static/             # Static analysis results
│   │   ├── video/              # Processed videos
│   │   └── video_true/         # Ground truth videos
│   └── fault/                  # Error analysis
│       ├── fn.txt              # False negatives
│       └── fp.txt              # False positives
├── Data/                       # Training and test datasets
│   ├── Dataset/                # Main dataset
│   │   ├── Focus Cam/          # Focus camera footage
│   │   ├── train/              # Training data
│   │   ├── val/                # Validation data
│   │   └── test/               # Test data
│   ├── Action Spotting/        # Action spotting datasets
│   │   ├── germany_bundesliga/
│   │   ├── italy_serie-a/
│   │   └── spain_laliga/
│   ├── Event Match/            # Match event data
│   │   ├── england_epl/
│   │   ├── europe_uefa-champions-league/
│   │   ├── france_ligue-1/
│   │   ├── germany_bundesliga/
│   │   ├── italy_serie-a/
│   │   └── spain_laliga/
│   └── MVF/                    # Multi-view foul dataset
└── Documentation/              # Research papers and presentations
    ├── *.pdf                   # Research papers
    └── *.png                   # Diagrams and illustrations
```

## 🚀 Features

- **Automated Frame Extraction**: Extract frames from videos at specified intervals
- **Multi-format Support**: Process various video formats (MP4, etc.)
- **Vision Transformer Integration**: Leverage state-of-the-art ViT models for feature extraction
- **Custom Augmentation**: Data augmentation specifically designed for sports footage
- **Multi-league Support**: Trained on data from multiple football leagues
- **Real-time Processing**: Efficient processing pipeline for video analysis
- **Result Visualization**: Generate visual outputs and analysis reports

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- CUDA-compatible GPU (recommended for model inference)

### Dependencies

```bash
# Core dependencies
pip install opencv-python
pip install moviepy
pip install imageio
pip install torch torchvision
pip install transformers
pip install numpy pandas
pip install matplotlib seaborn
pip install scikit-learn
pip install PyYAML
```

### Setup

1. Clone the repository:
```bash
git clone https://github.com/DucHiepisme/Final-Thesis.git
cd Final-Thesis
```

2. Create a virtual environment (recommended):
```bash
python -m venv thesis_env
# On Windows:
thesis_env\Scripts\activate
# On macOS/Linux:
source thesis_env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file or set OpenAI API key if using AI features
   - Configure paths in `src/constants.py` if needed

5. Download the pre-trained model (if not included):
   - The trained ViT model should be placed in `Code/cache/vit_custom_augmented_focuscam/`

## 🎮 Usage

### Basic Usage

Run the main pipeline:
```bash
cd Code
python main.py
```

### Frame Extraction

Extract frames from videos:
```python
from src.preprocess.frame_collector import FrameCollector

collector = FrameCollector()
collector.get_frame(input_dir="path/to/videos", output_path="path/to/output")
```

### Custom Configuration

Modify `config/prompt.yml` to adjust:
- Frame extraction intervals
- Model parameters
- Output directories
- Processing settings

## 📊 Model Performance

The system uses a custom-augmented Vision Transformer (ViT) model trained on focus camera footage:

- **Architecture**: Vision Transformer (ViT)
- **Training Data**: Multi-league football datasets
- **Augmentation**: Custom augmentation for sports scenarios
- **Performance Metrics**: Available in `cache/vit_custom_augmented_focuscam/eval_results.json`

## 🔬 Research Context

This project is part of a final thesis focusing on:
- Computer vision applications in sports
- Automated referee assistance systems
- Action recognition in football videos
- Real-time foul detection algorithms

### Related Papers
- Vision Transformer applications in sports analysis
- Action spotting in football videos
- Multi-view foul detection systems

## 📈 Results

The system generates several types of output:
- **Frame Analysis**: Individual frame classifications
- **Video Highlights**: Detected foul moments
- **Statistical Reports**: Performance metrics and analysis
- **Visualization**: Attention maps and detection confidence

## 🤝 Contributing

This is a thesis project, but suggestions and improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is part of an academic thesis. Please contact the author for usage permissions.

## 👨‍💻 Author

**DucHiepisme**
- GitHub: [@DucHiepisme](https://github.com/DucHiepisme)
- Project: Final Thesis - Football Foul Detection System

## 🙏 Acknowledgments

- Football datasets from major European leagues
- Vision Transformer research community
- Sports analytics research groups
- Academic supervisors and collaborators

## 📞 Contact

For questions about this thesis project, please contact the author through GitHub or academic channels.

---

*This project represents the culmination of research in computer vision applications for sports analysis, specifically focusing on automated foul detection in football matches.*
