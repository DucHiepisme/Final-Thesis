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
│   └── fault/                  # Error analysis
│       ├── fn.txt              # False negatives
│       └── fp.txt              # False positives
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
