if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Deepu316/Flash_Offical.git /Flash_offical
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Flash_offical
fi
cd /Spider-Official
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
