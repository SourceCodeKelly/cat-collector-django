from django.shortcuts import render
from django.template import Template
from django.views import View #
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
#...
class About(TemplateView):
    template_name = 'about.html'
    
class Cat:
    def __init__(self, name, image, size, weight, lifespan, intelligence, activity, coat, vocalness, info):
        self.name = name
        self.image = image
        self.size = size
        self.weight = weight
        self.lifespan = lifespan
        self.intelligence = intelligence
        self.activity = activity
        self.coat = coat
        self.vocalness = vocalness
        self.info = info
        
class CatList(TemplateView):
    template_name = 'cat_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = cats
        return context 
        
        
cats = [
    Cat('Bengal', 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FBENGAL-Profile.png&w=640&h=428&c=sc&poi=face&q=60', '8-10 inches', '9-15 pounds', '9-15 years', 'high', 'active', 'short', 'frequent', "The first time you see a Bengal cat roaming through your house, you might think a jungle cat has broken in. That's because this spectacular breed sports a spotted or marbled coat that looks a lot like a wild leopard or ocelot. But the Bengal is anything but wild, and has a loving, affectionate personality. While Bengals were developed by breeding domestic felines to an Asian leopard cat, their wild natures have long been abandoned.\n\nBengal cats were first accepted as a breed in 1983, and since then this handsome cat has skyrocketed in popularity. Like some other hybrid breeds, such as the Savannah cat, Bengal cats are classified by how many generations they are removed from their original wild parent. The kitten of the Asian leopard is called an F1. And every following generation gets a numerical designation such as F2, F3, F4, etc. To be considered a truly domestic cat, a Bengal must be at least an F4."),
    
    Cat('Scottish Fold (Highland Fold)', 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FSCOTTISH.FOLD-Profile.png&w=640&h=428&c=sc&poi=face&q=60', '8-10 inches', '6-9 pounds (female)/ 9-13 pounds (male)', '11 to 14 years', 'high', 'calm', 'long, short', 'when necessary', "Scottish folds are rare felines, prized for their huggable good looks and sweet personalities. Sporting round heads with tight, forward-facing folded ears and large eyes, Scottish folds always draw a lot of attention.\n\nScottish fold cats are a medium-sized cat breed weighing 6–12 pounds. They're low-maintenance and love being with their people more than anything else in the world. They're smart, too, and love playing games or chasing toys around the house.\n\nMarilyn Krieger, a Certified Cat Behavior Consultant in San Francisco known as The Cat Coach and author of Naughty No More: Change Unwanted Behaviors Through Positive Reinforcement, says it's important to do research and always purchase breeds of cats, such as the Scottish fold, from reputable breeders."),
    
    Cat("British Shorthair", "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FBRITISH.SHORTHAIR-Profile.png&w=640&h=428&c=sc&poi=face&q=60", "12-14 inches", "7-17 pounds", "15-20 years", "high", "calm", "short", "when necessary", "One of the most popular cat breeds in the world, the British shorthair is appropriately named. Not only do they have a thick, plush short coat, they also have a friendly yet no-nonsense—that is, rather British—sensibility about life. British shorthairs make ideal family cats and enjoy being with their owners, but may turn up their noses at being held or cuddled too much.\n\nThis beautiful breed comes in a wide variety of colors and patterns, but the traditional British shorthair is wrapped in blue fur. The best part: This medium-to-large-sized cat has few health problems."),
    
    Cat("Savannah Cat", "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FSAVANNAH-Profile.png&w=640&h=428&c=sc&poi=face&q=60", "14-17 inches", "12-25 pounds", "12-20 years", "high", "active", "short", "frequent", "Tall and elegant, the Savannah cat was first introduced in the late 20th century. Savannahs are actually a hybrid breed, the result of breeding a Siamese cat with a wild serval. And that wildness is on full display: The breed retains the large perked ears, long legs, and spotted coat of its African cat heritage, while keeping the friendly demeanor of a domestic pet.\n\nOne thing to know about Savannahs: These kitties are big. Adult Savannah cats can grow up to 17 inches tall and weigh 25 pounds, depending on generation. First generation crosses (called F1 and F2) are generally larger than later crosses and have beautiful spotted coats in shades of brown, tan, and black. Later generations are further removed from their wild ancestor, yet retain the colors and patterns of earlier generations—they're just smaller and a bit more docile. Savannah cats are loyal, intelligent, and inquisitive kitties, but might not be the best choice for first-time cat owners.\n\nThough they were introduced a couple decades ago, Savannah cats are still a relatively rare breed. A few states even have restrictions on them, often depending on generation. Checking state ordinances is a good idea before bringing home a Savannah cat."),
    
    Cat("Persian", "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FPERSIAN-Profile.png&w=640&h=428&c=sc&poi=face&q=60", "10-15 inches", "7-13 pounds", "10-15 years", "medium", "calm", "long", "quiet", "As one of the most recognized and adored cat breeds on the planet, Persian cats have been happily snuggling up with their owners since the 1600s. With their long, flowing coats; thick bodies; and flat faces, it's hard to resist the charm of a Persian.\n\nPersian cats are a medium-sized breed and take their role as a loving companion seriously-they're always ready to be stroked and fussed over on a moment's notice. This beautiful kitty comes in a wide variety of colors and color combos, and they get along with all family members (including fellow furry ones) when introduced as kittens. If you're willing to put in the work with grooming-and it's a lot of work-you won't find a more loving companion."),
    
    Cat("Siamese", "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F08%2F05%2FSIAMESE-Profile.png&w=640&h=428&c=sc&poi=face&q=60", "8-10 inches", "6-14 pounds", "15-20 years", "high", "active", "short", "howler", "The Siamese cat is a bright, intelligent feline with a handsome appearance and charming personality who can't help but draw admirers wherever he goes. These cats are known for being rather dog-like, and love attention—human affection is one thing this breed can't get enough of.\n\nSiamese kittens typically cost anywhere between $250–$1,000 and are a fairly popular breed. In 2018, the Siamese was the 13th most registered cat breed with the Cat Fanciers' Association. With their affectionate (and chatty!) personalities, it's easy to see why they're so beloved.")
]
        
