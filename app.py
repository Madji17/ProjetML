{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3bcd803e-6519-4f41-80df-023a49338d4a",
   "metadata": {},
   "source": [
    "### Partie 4: Code pour l'application Streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "55fbdb04-017c-469f-8c0f-5878a6ea1af3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-10 16:45:10.772 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\P1\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# Création du fichier app.py pour Streamlit\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Chargement du modèle et du scaler\n",
    "with open('mobile_price_model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "    \n",
    "with open('scaler.pkl', 'rb') as file:\n",
    "    scaler = pickle.load(file)\n",
    "\n",
    "# Titre de l'application\n",
    "st.title('PREDICTION DE LA GAMME DE PRIX DES TELEPHONES MOBILES')\n",
    "st.write('Cette application prédit la gamme de prix d\\'un téléphone mobile en fonction de ses caractéristiques.')\n",
    "\n",
    "# Création des widgets pour les entrées utilisateur\n",
    "st.sidebar.header('Caractéristiques du téléphone')\n",
    "\n",
    "def user_input_features():\n",
    "    battery_power = st.sidebar.slider('Capacité de la batterie (mAh)', 500, 2000, 1000)\n",
    "    blue = st.sidebar.selectbox('Bluetooth', [0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')\n",
    "    clock_speed = st.sidebar.slider('Vitesse du processeur (GHz)', 0.5, 3.0, 1.5)\n",
    "    dual_sim = st.sidebar.selectbox('Double SIM', [0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')\n",
    "    fc = st.sidebar.slider('Caméra frontale (MP)', 0, 20, 5)\n",
    "    four_g = st.sidebar.selectbox('4G', [0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')\n",
    "    int_memory = st.sidebar.slider('Mémoire interne (Go)', 2, 64, 16)\n",
    "    m_dep = st.sidebar.slider('Épaisseur (cm)', 0.1, 1.0, 0.5)\n",
    "    mobile_wt = st.sidebar.slider('Poids (g)', 80, 200, 140)\n",
    "    n_cores = st.sidebar.slider('Nombre de cœurs', 1, 8, 4)\n",
    "    pc = st.sidebar.slider('Caméra principale (MP)', 0, 20, 10)\n",
    "    px_height = st.sidebar.slider('Hauteur en pixels', 0, 1960, 1000)\n",
    "    px_width = st.sidebar.slider('Largeur en pixels', 0, 1960, 1000)\n",
    "    ram = st.sidebar.slider('RAM (Mo)', 256, 4000, 1000)\n",
    "    sc_h = st.sidebar.slider('Hauteur de l\\'écran (cm)', 5, 20, 12)\n",
    "    sc_w = st.sidebar.slider('Largeur de l\\'écran (cm)', 0, 18, 8)\n",
    "    talk_time = st.sidebar.slider('Autonomie en conversation (h)', 2, 20, 8)\n",
    "    three_g = st.sidebar.selectbox('3G', [0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')\n",
    "    touch_screen = st.sidebar.selectbox('Écran tactile', [0, 1], format_func=lambda x: 'Non' if x == 0 else 'Oui')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f394cc53-6b1f-45d9-a5b6-d136cc807617",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
