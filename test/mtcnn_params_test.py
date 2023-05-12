from PIL import Image
from torch import dist
from facenet_pytorch import MTCNN, InceptionResnetV1

resnet_vgg = InceptionResnetV1(pretrained='vggface2').eval()
resnet_casia = InceptionResnetV1(pretrained='casia-webface').eval()
mtcnn160 = MTCNN(image_size=160, margin=0, min_face_size=10)
mtcnn300 = MTCNN(image_size=300, margin=0, min_face_size=10)
mtcnn500 = MTCNN(image_size=500, margin=0, min_face_size=10)
mtcnn640 = MTCNN(image_size=640, margin=0, min_face_size=10)
mtcnn1000 = MTCNN(image_size=1000, margin=0, min_face_size=10)

database_photo_path = "db.jpg"
test_photo_true_path = "test_true.jpg"
test_photo_false_path = "test_false.jpg"

database_photo = Image.open(database_photo_path)
test_photo_true = Image.open(test_photo_true_path)
test_photo_false = Image.open(test_photo_false_path)

database_photo_face160 = mtcnn160(database_photo)
database_photo_emb160_vgg = resnet_vgg(database_photo_face160.unsqueeze(0)).detach()
database_photo_emb160_casia = resnet_casia(database_photo_face160.unsqueeze(0)).detach()

database_photo_face300 = mtcnn300(database_photo)
database_photo_emb300_vgg = resnet_vgg(database_photo_face300.unsqueeze(0)).detach()
database_photo_emb300_casia = resnet_casia(database_photo_face300.unsqueeze(0)).detach()

database_photo_face500 = mtcnn500(database_photo)
database_photo_emb500_vgg = resnet_vgg(database_photo_face500.unsqueeze(0)).detach()
database_photo_emb500_casia = resnet_casia(database_photo_face500.unsqueeze(0)).detach()

database_photo_face640 = mtcnn640(database_photo)
database_photo_emb640_vgg = resnet_vgg(database_photo_face640.unsqueeze(0)).detach()
database_photo_emb640_casia = resnet_casia(database_photo_face640.unsqueeze(0)).detach()

database_photo_face1000 = mtcnn1000(database_photo)
database_photo_emb1000_vgg = resnet_vgg(database_photo_face1000.unsqueeze(0)).detach()
database_photo_emb1000_casia = resnet_casia(database_photo_face1000.unsqueeze(0)).detach()

test_photo_true_face160 = mtcnn160(test_photo_true)
test_photo_true_emb160_vgg = resnet_vgg(test_photo_true_face160.unsqueeze(0)).detach()
test_photo_true_emb160_casia = resnet_casia(test_photo_true_face160.unsqueeze(0)).detach()

test_photo_true_face300 = mtcnn300(test_photo_true)
test_photo_true_emb300_vgg = resnet_vgg(test_photo_true_face300.unsqueeze(0)).detach()
test_photo_true_emb300_casia = resnet_casia(test_photo_true_face300.unsqueeze(0)).detach()

test_photo_true_face500 = mtcnn500(test_photo_true)
test_photo_true_emb500_vgg = resnet_vgg(test_photo_true_face500.unsqueeze(0)).detach()
test_photo_true_emb500_casia = resnet_casia(test_photo_true_face500.unsqueeze(0)).detach()

test_photo_true_face640 = mtcnn640(test_photo_true)
test_photo_true_emb640_vgg = resnet_vgg(test_photo_true_face640.unsqueeze(0)).detach()
test_photo_true_emb640_casia = resnet_casia(test_photo_true_face640.unsqueeze(0)).detach()

test_photo_true_face1000 = mtcnn1000(test_photo_true)
test_photo_true_emb1000_vgg = resnet_vgg(test_photo_true_face1000.unsqueeze(0)).detach()
test_photo_true_emb1000_casia = resnet_casia(test_photo_true_face1000.unsqueeze(0)).detach()

test_photo_false_face160 = mtcnn160(test_photo_false)
test_photo_false_emb160_vgg = resnet_vgg(test_photo_false_face160.unsqueeze(0)).detach()
test_photo_false_emb160_casia = resnet_casia(test_photo_false_face160.unsqueeze(0)).detach()

test_photo_false_face300 = mtcnn300(test_photo_false)
test_photo_false_emb300_vgg = resnet_vgg(test_photo_false_face300.unsqueeze(0)).detach()
test_photo_false_emb300_casia = resnet_casia(test_photo_false_face300.unsqueeze(0)).detach()

test_photo_false_face500 = mtcnn500(test_photo_false)
test_photo_false_emb500_vgg = resnet_vgg(test_photo_false_face500.unsqueeze(0)).detach()
test_photo_false_emb500_casia = resnet_casia(test_photo_false_face500.unsqueeze(0)).detach()

test_photo_false_face640 = mtcnn640(test_photo_false)
test_photo_false_emb640_vgg = resnet_vgg(test_photo_false_face640.unsqueeze(0)).detach()
test_photo_false_emb640_casia = resnet_casia(test_photo_false_face640.unsqueeze(0)).detach()

test_photo_false_face1000 = mtcnn1000(test_photo_false)
test_photo_false_emb1000_vgg = resnet_vgg(test_photo_false_face1000.unsqueeze(0)).detach()
test_photo_false_emb1000_casia = resnet_casia(test_photo_false_face1000.unsqueeze(0)).detach()

print("Results on size = 160, pretrained = vgg:")
print("True face: ", dist(database_photo_emb160_vgg, test_photo_true_emb160_vgg).item(),
      " False face: ", dist(database_photo_emb160_vgg, test_photo_false_emb160_vgg).item())
print("Results on size = 160, pretrained = casia:")
print("True face: ", dist(database_photo_emb160_casia, test_photo_true_emb160_casia).item(),
      " False face: ", dist(database_photo_emb160_casia, test_photo_false_emb160_casia).item())

print("\nResults on size = 300, pretrained = vgg:")
print("True face: ", dist(database_photo_emb300_vgg, test_photo_true_emb300_vgg).item(),
      " False face: ", dist(database_photo_emb300_vgg, test_photo_false_emb300_vgg).item())
print("Results on size = 300, pretrained = casia:")
print("True face: ", dist(database_photo_emb300_casia, test_photo_true_emb300_casia).item(),
      " False face: ", dist(database_photo_emb300_casia, test_photo_false_emb300_casia).item())

print("\nResults on size = 500, pretrained = vgg:")
print("True face: ", dist(database_photo_emb500_vgg, test_photo_true_emb500_vgg).item(),
      " False face: ", dist(database_photo_emb500_vgg, test_photo_false_emb500_vgg).item())
print("Results on size = 500, pretrained = casia:")
print("True face: ", dist(database_photo_emb500_casia, test_photo_true_emb500_casia).item(),
      " False face: ", dist(database_photo_emb500_casia, test_photo_false_emb500_casia).item())

print("\nResults on size = 640, pretrained = vgg:")
print("True face: ", dist(database_photo_emb640_vgg, test_photo_true_emb640_vgg).item(),
      " False face: ", dist(database_photo_emb640_vgg, test_photo_false_emb640_vgg).item())
print("Results on size = 640, pretrained = casia:")
print("True face: ", dist(database_photo_emb640_casia, test_photo_true_emb640_casia).item(),
      " False face: ", dist(database_photo_emb640_casia, test_photo_false_emb640_casia).item())

print("\nResults on size = 1000, pretrained = vgg:")
print("True face: ", dist(database_photo_emb1000_vgg, test_photo_true_emb1000_vgg).item(),
      " False face: ", dist(database_photo_emb1000_vgg, test_photo_false_emb1000_vgg).item())
print("Results on size = 1000, pretrained = casia:")
print("True face: ", dist(database_photo_emb1000_casia, test_photo_true_emb1000_casia).item(),
      " False face: ", dist(database_photo_emb1000_casia, test_photo_false_emb1000_casia).item())
