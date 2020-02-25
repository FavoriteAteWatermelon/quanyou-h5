<template>
  <div ref="wrapper">
		<slot></slot>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
export default {
	props: {
		probeType: {
			type: Number,
			default () {
				return 1
			}
		},
		canClick: {
			type: Boolean,
			default: true
		}
	},
	mounted () {
		this.$nextTick(() => {
			this._initScroll()
		})
	},
	methods: {
		_initScroll () {
			if (!this.$refs.wrapper) {
				return
			}
			this.scroll = new BScroll(this.$refs.wrapper, {
				probeType: this.probeType,
				click: this.canClick
			})
		}
	}
}
</script>

<style lang="stylus" scoped>

</style>