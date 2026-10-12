# File này KHÔNG chạy trong game.
# Nó chỉ tồn tại để Template Generation quét được tên và mô tả của các bể,
# vì Godot không quét chữ bên trong file .tres (data/environments/).
#
# Khi thêm / sửa bể trong data/environments/, cập nhật danh sách bên dưới
# rồi Generate lại messages.pot.
extends Object


func _strings() -> void:
	# Footer selector: gán trong code không qua tr()
	tr("You're here")
	# ac
	tr("Ancient Cold Lake")
	tr("An ultra-clear, icy lake full of ancient endemics.")
	# an
	tr("Antarctic Water")
	tr("An icy polar sea beneath the Antarctic ice.")
	# ap
	tr("Asian Peat Swamp")
	tr("Wine-dark peat water in a tropical swamp forest.")
	# ar
	tr("Arctic Water")
	tr("Cold, ice-grey Arctic shallows.")
	# bb
	tr("Billabong")
	tr("A teal Australian oxbow pool.")
	# bw
	tr("Blackwater")
	tr("A tea-coloured Amazon stream under amber light.")
	# by
	tr("Bayou")
	tr("Slow olive water among cypress roots.")
	# ce
	tr("Coral Reef")
	tr("A busy reef bursting with coral and colour.")
	# cn
	tr("Cenote")
	tr("A sunlit sinkhole of clear turquoise water.")
	# cs
	tr("Clear Spring")
	tr("Crystal-clear spring water over pale sand.")
	# cw
	tr("Cold Water")
	tr("A steel-blue northern sea, cold and rich.")
	# ds
	tr("Desert Spring")
	tr("A tiny warm spring hidden in the desert.")
	# dw
	tr("Deep Water")
	tr("Dark depths far below the sunlight.")
	# fs
	tr("Forest Stream")
	tr("A shaded woodland brook full of roots and moss.")
	# gu
	tr("Galapagos Upwelling")
	tr("Nutrient-rich currents around volcanic islands.")
	# ha
	tr("High Andes Lake")
	tr("A cold, clear lake high in the Andes.")
	# hs
	tr("Hillstream")
	tr("Fast, oxygen-rich rapids over smooth pebbles.")
	# hv
	tr("Hydrothermal Vent")
	tr("Black smokers glowing on the deep-sea floor.")
	# kf
	tr("Kelp Forest")
	tr("Tall golden-green kelp in cool coastal water.")
	# kp
	tr("Koi Pond")
	tr("A calm garden pond with jade-green water.")
	# mg
	tr("Mangrove")
	tr("Tangled mangrove roots where the sea meets the land.")
	# mk
	tr("Muck Sand")
	tr("Dark volcanic sand hiding strange critters.")
	# mr
	tr("Muddy River")
	tr("A murky lowland river with soft silt banks.")
	# ms
	tr("Marsh Swamp")
	tr("Still, weedy wetland water under green shade.")
	# ob
	tr("Ocean")
	tr("Open blue water near the sea surface.")
	# op
	tr("Open Pelagic")
	tr("Endless blue open ocean.")
	# pf
	tr("Planted Freshwater")
	tr("A bright, plant-filled tank of clear water.")
	# rc
	tr("Rocky Coast")
	tr("Wave-washed rocks and tide pools.")
	# rl
	tr("Rift Lake")
	tr("A deep blue African lake with rocky reefs.")
	# rr
	tr("Rocky River")
	tr("Cool, fast water over smooth river stones.")
	# sg
	tr("Seagrass Meadow")
	tr("Swaying seagrass beds in sunlit shallows.")
	# sp
	tr("Cold Seep")
	tr("Methane seeps on the dark ocean floor.")
	# sr
	tr("Sargassum Sea")
	tr("Floating golden seaweed mats far out at sea.")
	# tp
	tr("Tropical")
	tr("Warm, clear tropical shallows.")
	# tz
	tr("Twilight Zone")
	tr("Dim midwater where the light fades to black.")
	# uc
	tr("Underwater Cave")
	tr("A pitch-dark flooded cave.")
