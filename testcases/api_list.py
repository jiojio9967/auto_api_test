# -*- coding: utf-8 -*-

api_list = [
    # 盲盒-奖励兑换
    ("GET", "/xhj-gather-app/activityAwardRecord/blindBoxConversion"),
    # 内容传播-奖励兑换
    ("POST", "/xhj-gather-app/activityAwardRecord/conversion"),
    # 内容传播-奖励记录头部
    ("GET", "/xhj-gather-app/activityAwardRecord/queryHeader"),
    # 内容传播-奖励记录分页列表
    ("POST", "/xhj-gather-app/activityAwardRecord/queryPage"),
    # 用户认证审核保存
    ("POST", "/xhj-gather-app/activityMemberAuthReview/save"),
    # 内容传播-分享审核分页
    ("POST", "/xhj-gather-app/activityShareReview/queryPage"),
    # 内容传播-分享审核保存
    ("POST", "/xhj-gather-app/activityShareReview/save"),
    # AI-快讯生成文章
    ("POST", "/xhj-gather-app/aiGen/genNewsFlashToArticle"),
    # 收藏
    ("POST", "/xhj-gather-app/articleCollect/collect"),
    # 分页列表
    ("GET", "/xhj-gather-app/articleCollect/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/articleCollect/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消收藏
    ("POST", "/xhj-gather-app/articleCollect/unCollect"),
    # 点赞
    ("POST", "/xhj-gather-app/articleCommentLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/articleCommentLike/unLike"),
    # 批量删除
    ("POST", "/xhj-gather-app/articleDraft/deleteByIds"),
    # 详情
    ("GET", "/xhj-gather-app/articleDraft/detail", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 详情
    ("POST", "/xhj-gather-app/articleDraft/detail", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("GET", "/xhj-gather-app/articleDraft/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/articleDraft/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 保存
    ("POST", "/xhj-gather-app/articleDraft/save"),
    # 保存视频
    ("POST", "/xhj-gather-app/articleDraft/saveVideo"),
    # 点赞
    ("POST", "/xhj-gather-app/articleLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/articleLike/unLike"),
    # 更新AI总结反馈状态
    ("POST", "/xhj-gather-app/articleSynopsisFeedback/auth/putUsefulFlag"),
    # 收藏
    ("POST", "/xhj-gather-app/celebrity/contentCollect/collect"),
    # 分页列表
    ("POST", "/xhj-gather-app/celebrity/contentCollect/page"),
    # 取消收藏
    ("POST", "/xhj-gather-app/celebrity/contentCollect/unCollect"),
    # 评论
    ("POST", "/xhj-gather-app/celebrity/contentComment/save"),
    # 点赞
    ("POST", "/xhj-gather-app/celebrity/contentCommentLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/celebrity/contentCommentLike/unLike"),
    # 点赞
    ("POST", "/xhj-gather-app/celebrity/contentLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/celebrity/contentLike/unLike"),
    # 关注
    ("POST", "/xhj-gather-app/celebrity/follow/follow"),
    # 分页列表
    ("POST", "/xhj-gather-app/celebrity/follow/page"),
    # 取消关注
    ("POST", "/xhj-gather-app/celebrity/follow/unFollow"),
    # 获取社区动态评论
    ("POST", "/xhj-gather-app/chatGpt/getCommunityContentComment"),
    # 发送
    ("POST", "/xhj-gather-app/chatGpt/send"),
    # 发送
    ("POST", "/xhj-gather-app/chatGpt/sendStream"),
    # 发送
    ("POST", "/xhj-gather-app/chatGpt/sendStreamV2"),
    # 发送
    ("POST", "/xhj-gather-app/chatGpt/sendStreamV3"),
    # chatGpt用户问答记录分页列表
    ("GET", "/xhj-gather-app/chatRecord/getChatMemberRecordPage", {'limit': 10, 'page': 1}),
    # ai问答未读记录数
    ("GET", "/xhj-gather-app/chatRecord/getUnreadNum"),
    # 设置全部已读
    ("POST", "/xhj-gather-app/chatRecord/putAllRead"),
    # 保存
    ("POST", "/xhj-gather-app/cms/article/save"),
    # 保存视频
    ("POST", "/xhj-gather-app/cms/article/saveVideo"),
    # 作者订阅
    ("POST", "/xhj-gather-app/cms/articleAuthorFollow/follow"),
    # 已关注作者文章列表
    ("GET", "/xhj-gather-app/cms/articleAuthorFollow/followKolArticlePage", {'limit': 10, 'page': 1}),
    # 取消作者订阅
    ("POST", "/xhj-gather-app/cms/articleAuthorFollow/unFollow"),
    # 内容快讯看涨看跌操作
    ("POST", "/xhj-gather-app/cms/newsflashLike/downUp"),
    # 专题取消订阅
    ("POST", "/xhj-gather-app/cms/newsflashTopic/cancelSubscribe"),
    # 专题订阅
    ("POST", "/xhj-gather-app/cms/newsflashTopic/subscribe"),
    # 获取标签列表
    ("GET", "/xhj-gather-app/cms/tag/stateless/getTagList"),
    # 收藏
    ("POST", "/xhj-gather-app/cmsNewsFlashCollect/collect"),
    # 快讯-收藏分页列表
    ("GET", "/xhj-gather-app/cmsNewsFlashCollect/collectPage", {'limit': 10, 'page': 1}),
    # 取消收藏
    ("POST", "/xhj-gather-app/cmsNewsFlashCollect/unCollect"),
    # 详情
    ("GET", "/xhj-gather-app/coin/contract/detail"),
    # K线对决
    ("GET", "/xhj-gather-app/coin/currencyHistory/duel"),
    # 关注
    ("POST", "/xhj-gather-app/coin/plateFollow/follow"),
    # 取消关注
    ("POST", "/xhj-gather-app/coin/plateFollow/unFollow"),
    # 删除
    ("POST", "/xhj-gather-app/coin/wait/del"),
    # 保存
    ("POST", "/xhj-gather-app/coin/wait/save"),
    # 更新
    ("POST", "/xhj-gather-app/coin/wait/update"),
    # 根据清单列表ID获取币列表
    ("GET", "/xhj-gather-app/coin/waitCurrency/getByWaitId", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 根据清单列表ID获取币列表
    ("POST", "/xhj-gather-app/coin/waitCurrency/getByWaitId", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 保存
    ("POST", "/xhj-gather-app/coin/waitCurrency/save"),
    # 关注
    ("POST", "/xhj-gather-app/coin/waitFollow/follow"),
    # 取消关注
    ("POST", "/xhj-gather-app/coin/waitFollow/unFollow"),
    # 评论我的动态
    ("GET", "/xhj-gather-app/community/content/commentMePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 我评论的动态
    ("GET", "/xhj-gather-app/community/content/commentPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 点赞我的动态
    ("GET", "/xhj-gather-app/community/content/likeMePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 我点赞的动态
    ("GET", "/xhj-gather-app/community/content/likePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 保存
    ("POST", "/xhj-gather-app/community/content/save"),
    # 发表弹幕
    ("POST", "/xhj-gather-app/community/contentBullet/save"),
    # 收藏
    ("POST", "/xhj-gather-app/community/contentCollect/collect"),
    # 分页列表
    ("GET", "/xhj-gather-app/community/contentCollect/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/community/contentCollect/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消收藏
    ("POST", "/xhj-gather-app/community/contentCollect/unCollect"),
    # 回答-回复我的
    ("GET", "/xhj-gather-app/community/contentComment/questionCommentMinePage", {'limit': 10, 'page': 1}),
    # 我的回答
    ("GET", "/xhj-gather-app/community/contentComment/questionCommentPage", {'limit': 10, 'page': 1}),
    # 回答-赞我的
    ("GET", "/xhj-gather-app/community/contentComment/questionLikeMinePage", {'limit': 10, 'page': 1}),
    # 点赞
    ("POST", "/xhj-gather-app/community/contentCommentLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/community/contentCommentLike/unLike"),
    # 批量删除
    ("POST", "/xhj-gather-app/community/contentDraft/deleteByIds"),
    # 详情
    ("GET", "/xhj-gather-app/community/contentDraft/detail", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 详情
    ("POST", "/xhj-gather-app/community/contentDraft/detail", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("GET", "/xhj-gather-app/community/contentDraft/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/community/contentDraft/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 保存
    ("POST", "/xhj-gather-app/community/contentDraft/save"),
    # 批量邀请
    ("POST", "/xhj-gather-app/community/contentInvitation/batchSave"),
    # 邀请分页列表
    ("GET", "/xhj-gather-app/community/contentInvitation/invitationPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 邀请分页列表
    ("POST", "/xhj-gather-app/community/contentInvitation/invitationPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 消息-受邀问答分页列表
    ("GET", "/xhj-gather-app/community/contentInvitation/invitationQuestionPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 消息-受邀问答分页列表
    ("POST", "/xhj-gather-app/community/contentInvitation/invitationQuestionPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 邀请
    ("POST", "/xhj-gather-app/community/contentInvitation/save"),
    # 点赞
    ("POST", "/xhj-gather-app/community/contentLike/like"),
    # 取消点赞
    ("POST", "/xhj-gather-app/community/contentLike/unLike"),
    # 关注
    ("POST", "/xhj-gather-app/community/topicFollow/follow"),
    # 分页列表
    ("GET", "/xhj-gather-app/community/topicFollow/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/community/topicFollow/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消关注
    ("POST", "/xhj-gather-app/community/topicFollow/unFollow"),
    # 管理页
    ("GET", "/xhj-gather-app/creatorContent/managePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 管理页
    ("POST", "/xhj-gather-app/creatorContent/managePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 内容分页列表
    ("GET", "/xhj-gather-app/creatorContent/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 内容分页列表
    ("POST", "/xhj-gather-app/creatorContent/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # Ai-收藏
    ("POST", "/xhj-gather-app/cueWord/collect"),
    # Ai-提示词列表
    ("GET", "/xhj-gather-app/cueWord/getQueryList"),
    # Ai-新增用户提示词
    ("POST", "/xhj-gather-app/cueWord/save"),
    # 收藏
    ("POST", "/xhj-gather-app/currencyCollect/collect"),
    # 批量收藏
    ("POST", "/xhj-gather-app/currencyCollect/collectList"),
    # 取消收藏
    ("POST", "/xhj-gather-app/currencyCollect/unCollect"),
    # 更新排序
    ("POST", "/xhj-gather-app/currencyCollect/update/sort"),
    # 获取最近一次提醒邮箱
    ("GET", "/xhj-gather-app/currencyNotice/getEmail"),
    # 大额提醒状态-单币种
    ("GET", "/xhj-gather-app/currencyNotice/largeStatus"),
    # 大额提醒状态-全币种
    ("GET", "/xhj-gather-app/currencyNotice/largeStatusAll"),
    # 提醒分页列表
    ("GET", "/xhj-gather-app/currencyNotice/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 提醒分页列表
    ("POST", "/xhj-gather-app/currencyNotice/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 大额提醒分页列表
    ("GET", "/xhj-gather-app/currencyNotice/pageLarge", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 提醒分页列表
    ("GET", "/xhj-gather-app/currencyNotice/pageV2", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 保存提醒
    ("POST", "/xhj-gather-app/currencyNotice/save"),
    # 批量保存大额提醒
    ("POST", "/xhj-gather-app/currencyNotice/saveBatchLarge"),
    # 更新大额提醒
    ("POST", "/xhj-gather-app/currencyNotice/updateLarge"),
    # 提醒记录分页列表
    ("GET", "/xhj-gather-app/currencyNoticeRecord/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 看跌
    ("POST", "/xhj-gather-app/currencyOpinion/down"),
    # 看涨
    ("POST", "/xhj-gather-app/currencyOpinion/up"),
    # 列表
    ("GET", "/xhj-gather-app/defaultMessage/list"),
    # 收藏
    ("POST", "/xhj-gather-app/exchangeCollect/collect"),
    # 是否收藏
    ("POST", "/xhj-gather-app/exchangeCollect/isCollect"),
    # 取消收藏
    ("POST", "/xhj-gather-app/exchangeCollect/unCollect"),
    # 保存
    ("POST", "/xhj-gather-app/feedback/save"),
    # 群聊顶部
    ("GET", "/xhj-gather-app/im/group/banner"),
    # 群聊顶部
    ("GET", "/xhj-gather-app/im/group/bannerV2"),
    # 详情
    ("GET", "/xhj-gather-app/im/group/detail"),
    # 我的群
    ("GET", "/xhj-gather-app/im/group/mine", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 更多群聊
    ("GET", "/xhj-gather-app/im/group/more", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 推荐群聊
    ("GET", "/xhj-gather-app/im/group/recommend"),
    # 机器人指令
    ("GET", "/xhj-gather-app/im/group/robotInstruct"),
    # 保存
    ("POST", "/xhj-gather-app/im/group/save"),
    # 群成员申请加入
    ("POST", "/xhj-gather-app/im/groupMember/add"),
    # 拉人
    ("POST", "/xhj-gather-app/im/groupMember/batchAdd"),
    # 移除群成员
    ("POST", "/xhj-gather-app/im/groupMember/del"),
    # 详情
    ("GET", "/xhj-gather-app/im/groupMember/detail"),
    # 审核
    ("POST", "/xhj-gather-app/im/groupMember/examine"),
    # 批量审核
    ("POST", "/xhj-gather-app/im/groupMember/examineBatch"),
    # 退群
    ("POST", "/xhj-gather-app/im/groupMember/quit"),
    # 确认群公告
    ("POST", "/xhj-gather-app/im/groupNotice/confirm"),
    # 最新群公告
    ("GET", "/xhj-gather-app/im/groupNotice/last", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 群公告
    ("GET", "/xhj-gather-app/im/groupNotice/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 群公告-保存
    ("POST", "/xhj-gather-app/im/groupNotice/save"),
    # save
    ("POST", "/xhj-gather-app/im/message/fail/save"),
    # 发送消息
    ("POST", "/xhj-gather-app/im/message/send"),
    # 分页列表
    ("GET", "/xhj-gather-app/label/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/label/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 销号
    ("POST", "/xhj-gather-app/member/destroy"),
    # 获取基本信息
    ("GET", "/xhj-gather-app/member/info"),
    # 获取基本信息
    ("POST", "/xhj-gather-app/member/info"),
    # 退出登录
    ("POST", "/xhj-gather-app/member/out"),
    # 更新账号(手机号或邮箱)
    ("POST", "/xhj-gather-app/member/updateAccount"),
    # 更新基本信息
    ("POST", "/xhj-gather-app/member/updateInfo"),
    # 更新手机号码
    ("POST", "/xhj-gather-app/member/updateMobile"),
    # 获取chat帐户可用次数
    ("GET", "/xhj-gather-app/memberAccount/getChat"),
    # 获取chat帐户可用次数
    ("POST", "/xhj-gather-app/memberAccount/getChat"),
    # 获取chat帐户可用次数-web
    ("GET", "/xhj-gather-app/memberAccount/getChatWeb"),
    # 获取chat帐户可用次数-web
    ("POST", "/xhj-gather-app/memberAccount/getChatWeb"),
    # 获取积分帐户可用数量
    ("GET", "/xhj-gather-app/memberAccount/getPoint"),
    # 获取积分帐户可用数量
    ("POST", "/xhj-gather-app/memberAccount/getPoint"),
    # 分页
    ("GET", "/xhj-gather-app/memberAccountJournal/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页
    ("POST", "/xhj-gather-app/memberAccountJournal/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 我的评论记录
    ("GET", "/xhj-gather-app/memberActivityCommentRecord/mine"),
    # 评论图片上传
    ("POST", "/xhj-gather-app/memberActivityCommentRecord/save"),
    # 我的竞猜记录
    ("GET", "/xhj-gather-app/memberActivityGuessRecord/mine", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 我的竞猜记录
    ("POST", "/xhj-gather-app/memberActivityGuessRecord/mine", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 竞猜
    ("POST", "/xhj-gather-app/memberActivityGuessRecord/save"),
    # 我的邀请记录
    ("GET", "/xhj-gather-app/memberActivityInviteRecord/mine", {'limit': 10, 'page': 1}),
    # 我的统计
    ("GET", "/xhj-gather-app/memberActivityInviteRecord/statistics"),
    # 待提现金额
    ("GET", "/xhj-gather-app/memberActivityReward/cashAmount"),
    # 风险识别
    ("POST", "/xhj-gather-app/memberActivityReward/check"),
    # 可抽奖次数
    ("GET", "/xhj-gather-app/memberActivityReward/count"),
    # 可抽奖次数（盲盒调整）
    ("GET", "/xhj-gather-app/memberActivityReward/countV2"),
    # 抽奖
    ("POST", "/xhj-gather-app/memberActivityReward/draw"),
    # 抽奖V2
    ("POST", "/xhj-gather-app/memberActivityReward/drawV2"),
    # 抽奖V3
    ("POST", "/xhj-gather-app/memberActivityReward/drawV3"),
    # 获取用户抽奖相关信息
    ("GET", "/xhj-gather-app/memberActivityReward/memberInfo"),
    # 中奖列表
    ("GET", "/xhj-gather-app/memberActivityReward/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 中奖列表
    ("POST", "/xhj-gather-app/memberActivityReward/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 盲盒活动-获取奖励列表
    ("POST", "/xhj-gather-app/memberActivityReward/queryBoxAward"),
    # 盲盒活动-头部信息
    ("GET", "/xhj-gather-app/memberActivityReward/queryBoxHeader"),
    # 盲盒活动-免费抽奖未读通知
    ("GET", "/xhj-gather-app/memberActivityReward/queryFreeDrawNoticeUnread"),
    # 盲盒活动-免费抽奖通知已读确认
    ("GET", "/xhj-gather-app/memberActivityReward/readFreeDrawNotice"),
    # 申请提现-转盘-钱包地址提现
    ("POST", "/xhj-gather-app/memberActivityRewardCash/apply"),
    # 空投-申请提现
    ("POST", "/xhj-gather-app/memberActivityRewardCash/applyAirdrop"),
    # 申请提现V2-单个活动
    ("POST", "/xhj-gather-app/memberActivityRewardCash/applyV2"),
    # 申请提现V3
    ("POST", "/xhj-gather-app/memberActivityRewardCash/applyV3"),
    # 历史提现地址
    ("GET", "/xhj-gather-app/memberActivityRewardCash/history"),
    # 获得上次提现数据
    ("GET", "/xhj-gather-app/memberActivityRewardCash/last"),
    # 签到
    ("POST", "/xhj-gather-app/memberActivitySignRecord/save"),
    # 参加空投
    ("POST", "/xhj-gather-app/memberAirdropRecord/save"),
    # 得分
    ("GET", "/xhj-gather-app/memberAirdropRecord/score"),
    # 获取用户应用市场评论记录详情
    ("GET", "/xhj-gather-app/memberAppRating/details"),
    # 获取用户是否有参与应用市场评论的资格
    ("GET", "/xhj-gather-app/memberAppRating/eligible"),
    # 我的兑换券
    ("GET", "/xhj-gather-app/memberAppRating/mine"),
    # 上传评论截图
    ("POST", "/xhj-gather-app/memberAppRating/saveScreenshot"),
    # 拉黑
    ("POST", "/xhj-gather-app/memberBlack/black"),
    # 分页列表
    ("GET", "/xhj-gather-app/memberBlack/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/memberBlack/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消拉黑
    ("POST", "/xhj-gather-app/memberBlack/unBlack"),
    # 详情
    ("GET", "/xhj-gather-app/memberCreator/detail"),
    # 保存
    ("POST", "/xhj-gather-app/memberCreator/save"),
    # 关注
    ("POST", "/xhj-gather-app/memberFollow/follow"),
    # 分页列表
    ("GET", "/xhj-gather-app/memberFollow/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/memberFollow/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消关注
    ("POST", "/xhj-gather-app/memberFollow/unFollow"),
    # 分页列表
    ("GET", "/xhj-gather-app/memberInvited/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 分页列表
    ("POST", "/xhj-gather-app/memberInvited/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 统计-邀请获得积分-积分获取比例
    ("GET", "/xhj-gather-app/memberInvited/statistics"),
    # 保存
    ("POST", "/xhj-gather-app/memberLabel/save"),
    # 保存
    ("POST", "/xhj-gather-app/memberPush/save"),
    # 清空阅读数量
    ("POST", "/xhj-gather-app/notice/clear"),
    # 评论通知列表
    ("GET", "/xhj-gather-app/notice/commentPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 评论通知列表
    ("POST", "/xhj-gather-app/notice/commentPage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 获取未读数量
    ("GET", "/xhj-gather-app/notice/count"),
    # 获取未读数量
    ("POST", "/xhj-gather-app/notice/count"),
    # 删除通知
    ("POST", "/xhj-gather-app/notice/delete"),
    # 点赞通知表
    ("GET", "/xhj-gather-app/notice/likePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 点赞通知表
    ("POST", "/xhj-gather-app/notice/likePage", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 批量上传文件
    ("POST", "/xhj-gather-app/oss/batchUpload"),
    # 获取token
    ("GET", "/xhj-gather-app/oss/getSts"),
    # 上传文件
    ("POST", "/xhj-gather-app/oss/upload"),
    # 兑换
    ("POST", "/xhj-gather-app/pointsEquity/exchange"),
    # 挖矿活动：获取会员矿机信息
    ("POST", "/xhj-gather-app/promActivityMining/getMemberMiningInfo"),
    # 挖矿活动：矿机配置列表查询
    ("POST", "/xhj-gather-app/promActivityMining/queryList"),
    # 挖矿活动：收益签到领取
    ("POST", "/xhj-gather-app/promActivityMiningMemberIncome/miningCheckIncome"),
    # 挖矿活动：获取会员当前矿机收益签到列表
    ("POST", "/xhj-gather-app/promActivityMiningMemberIncome/queryList"),
    # 挖矿活动：会员收益排行榜
    ("POST", "/xhj-gather-app/promActivityMiningMemberIncome/rankingListPage"),
    # 挖矿活动：用户矿机购买记录
    ("POST", "/xhj-gather-app/promActivityMiningMemberPurchase/getPurchaseMiningPageList"),
    # 挖矿活动：购买矿机
    ("POST", "/xhj-gather-app/promActivityMiningMemberPurchase/purchaseMining"),
    # 挖矿活动：提现记录
    ("POST", "/xhj-gather-app/promActivityMiningWithdrawal/auth/queryPage"),
    # 挖矿活动：创建提现券码
    ("POST", "/xhj-gather-app/promActivityMiningWithdrawal/auth/save"),
    # 挖矿活动：提现汇总信息
    ("POST", "/xhj-gather-app/promActivityMiningWithdrawal/auth/sumInfo"),
    # 举报列表
    ("GET", "/xhj-gather-app/report/list"),
    # 新增
    ("POST", "/xhj-gather-app/report/save"),
    # 收藏
    ("POST", "/xhj-gather-app/smartMoneyCollect/collect"),
    # 分页列表
    ("GET", "/xhj-gather-app/smartMoneyCollect/page", {'limit': 10, 'page': 1, 'pageSize': 10}),
    # 取消收藏
    ("POST", "/xhj-gather-app/smartMoneyCollect/unCollect"),
    # 多语言翻译配置删除
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/deleteByIds"),
    # 多语言翻译配置主键查询
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/getById"),
    # 多语言翻译配置列表查询
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/queryList"),
    # 多语言翻译配置分页列表
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/queryPage"),
    # 多语言翻译配置保存
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/save"),
    # 多语言翻译配置修改
    ("POST", "/xhj-gather-app/sysLanguageConfig/auth/updateById"),
    # browseArticle
    ("POST", "/xhj-gather-app/taskCenter/browseArticle"),
    # browseVideo
    ("POST", "/xhj-gather-app/taskCenter/browseVideo"),
    # getBrowseSec
    ("GET", "/xhj-gather-app/taskCenter/getBrowseSec"),
    # 任务上报
    ("POST", "/xhj-gather-app/taskCenter/report"),
    # 查询地址历史余额
    ("POST", "/xhj-gather-app/third/ok-link/address/address-balance-history"),
    # 删除地址监控任务
    ("GET", "/xhj-gather-app/third/ok-link/address/delete/address-monitor"),
    # 查询地址监控任务
    ("POST", "/xhj-gather-app/third/ok-link/address/query/address-monitor"),
    # 查询公链信息
    ("GET", "/xhj-gather-app/third/ok-link/address/query/chain"),
    # 富豪地址排行榜
    ("GET", "/xhj-gather-app/third/ok-link/address/rich"),
    # 查询地址授权代币列表
    ("POST", "/xhj-gather-app/third/ok-link/auth-token/address-list"),
    # 代币授权查询-头部信息
    ("GET", "/xhj-gather-app/third/ok-link/auth-token/header-info"),
    # 查询代币授权列表
    ("POST", "/xhj-gather-app/third/ok-link/auth-token/list"),
    # 查询代币合约地址列表
    ("POST", "/xhj-gather-app/third/ok-link/auth-token/query/token"),
]
