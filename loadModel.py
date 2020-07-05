import torch
from utils.helpers import *
import warnings
from PIL import Image
from torchvision import transforms

def image_transform(imagepath):
    test_transforms = transforms.Compose([transforms.Resize(255),
                                          transforms.CenterCrop(224),
                                          transforms.ToTensor(),
                                          transforms.Normalize([0.485, 0.456, 0.406],
                                                               [0.229, 0.224, 0.225])])
    image = Image.open(imagepath)
    imagetensor = test_transforms(image)
    return imagetensor


def predict(imagepath, verbose=False):
    if not verbose:
        warnings.filterwarnings('ignore')
    model_path = 'Model/rustNonrust.pth'
    model = load_model(model_path)
    model.eval()
    if verbose:
        print("Model Loaded..")
    image = image_transform(imagepath)
    image1 = image[None,:,:,:]
    ps=torch.exp(model(image1))
    topconf, topclass = ps.topk(1, dim=1)
    if topclass.item() == 1:
        return {'class':'Rust','confidence':str(topconf.item())}
    else:
        return {'class':'NonRust','confidence':str(topconf.item())}

print(predict('Data/validate/rust/165.jpg'))